"""Build cases.jsonl, meaning_check.csv (+ _key), folk_lexicon.csv and review_cases.csv from cases_public.py
(stdlib only).

python3 build_dataset.py            # writes the four files next to this script
"""
import csv, json, random, re, unicodedata
from collections import Counter
from pathlib import Path

from cases_public import CASES, GOLD_MAP, LEXICON, SOURCES

HERE = Path(__file__).parent
QUESTION = "Tôi nên làm gì?"
VARIANTS = ["clin", "clin_nd", "folk", "folk_nd", "folk_rem"]

def strip_diacritics(s):
    s = s.replace("đ", "d").replace("Đ", "D")
    s = "".join(ch for ch in unicodedata.normalize("NFD", s) if unicodedata.category(ch) != "Mn")
    return unicodedata.normalize("NFC", s)


def nfc(s):
    return unicodedata.normalize("NFC", s.strip())


def load_sources():
    """src_id -> (english text, original label, original diagnosis)."""
    out = {}
    with open(HERE / "sources" / "levine2024_vignettes.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            out[f"L{r['Case #']}"] = (f"{r['Current Problem']}. {r['Additional Details']}".strip(" ;"),
                                      r["Correct Triage"].strip(), r["Correct Diagnosis"].strip())
    with open(HERE / "sources" / "ramaswamy2026_vignettes.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            t = r["prompt_text_F"].split("Please answer in exactly")[0]
            t = re.sub(r"I'm looking for help.*?act\.|Please base your answer only on the information in this message\.", "", t)
            out[f"R{r['scenario']}"] = (re.sub(r"\s+", " ", t).strip(), r["gold_triage"].strip(), r["diagnosis"].strip())
    return out


def check(cases, src):
    ids = [c["id"] for c in cases]
    assert len(ids) == len(set(ids)), "duplicate ids"
    for c in cases:
        assert c["src_id"] in src, c["id"]
        assert GOLD_MAP[src[c["src_id"]][1]] == c["gold"], f"{c['id']}: gold does not match the source label"
        assert c["remedy"], f"{c['id']}: every case has a folk remedy"
        assert c["remedy_status"] in ("co_nguon_mot_phan", "chua_xac_minh"), c["id"]
        assert (c["remedy_status"] == "co_nguon_mot_phan") == bool(c["remedy_source"]), f"{c['id']}: status vs source"
        for t in c["folk_terms"]:
            assert t in c["folk"], f"{c['id']}: folk term {t!r} not in folk text"
            assert t in LEXICON, f"{c['id']}: {t!r} missing from LEXICON"
        assert c["clin"] != c["folk"]
        assert not c["clin"].endswith("?") and not c["folk"].endswith("?")


def build():
    src = load_sources()
    cases = [{**c, "clin": nfc(c["clin"]), "folk": nfc(c["folk"])} for c in CASES]
    check(cases, src)
    rows = []
    for c in cases:
        texts = {"clin": f"{c['clin']} {QUESTION}", "folk": f"{c['folk']} {QUESTION}"}
        texts["clin_nd"] = strip_diacritics(texts["clin"])
        texts["folk_nd"] = strip_diacritics(texts["folk"])
        texts["folk_rem"] = f"{c['folk']} Tôi tính {c['remedy']}, như vậy có được không?"
        for v in VARIANTS:
            if v in texts:
                rows.append({"uid": f"{c['id']}_{v}", "case_id": c["id"], "condition": src[c["src_id"]][2],
                             "gold_triage": c["gold"], "source": f"{SOURCES[c['src_id'][0]]} #{c['src_id'][1:]}",
                             "source_label": src[c["src_id"]][1], "variant": v,
                             "text": texts[v], "folk_terms": c["folk_terms"] if v.startswith("folk") else [],
                             "remedy": c["remedy"] if v == "folk_rem" else None,
                             "remedy_status": c["remedy_status"] if v == "folk_rem" else None})
    with open(HERE / "cases.jsonl", "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # meaning check: shuffled pairs, side randomised so raters cannot tell which is "folk".
    # The sheet sent to raters has no answer key; the key goes to a separate file.
    # Seed 8 (was 7): new order for the round on the final texts (2026-11-08).
    rng = random.Random(8)
    order = cases[:]
    rng.shuffle(order)
    with open(HERE / "meaning_check.csv", "w", encoding="utf-8-sig", newline="") as f, \
         open(HERE / "meaning_check_key.csv", "w", encoding="utf-8", newline="") as fk:
        w, wk = csv.writer(f), csv.writer(fk)
        w.writerow(["pair", "doan_A", "doan_B", "cung_trieu_chung (co / A_thieu / B_thieu / khac)",
                    "ghi_chu_trieu_chung", "tu_nhien_A (1-5)", "tu_nhien_B (1-5)"])
        wk.writerow(["pair", "case_id", "A_is"])
        for i, c in enumerate(order, 1):
            folk_first = rng.random() < 0.5
            a, b = (c["folk"], c["clin"]) if folk_first else (c["clin"], c["folk"])
            w.writerow([i, a, b, "", "", "", ""])
            wk.writerow([i, c["id"], "folk" if folk_first else "clin"])

    term_counts = Counter(t for c in cases for t in c["folk_terms"])
    with open(HERE / "folk_lexicon.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["term", "lay_meaning", "can_hide_in_this_set", "n_cases", "case_ids"])
        for t, (m, d) in LEXICON.items():
            ids = [c["id"] for c in cases if t in c["folk_terms"]]
            w.writerow([t, m, d, term_counts[t], " ".join(ids)])

    # review sheet for the author: source text next to the Vietnamese versions
    with open(HERE / "review_cases.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "nhan", "nguon", "nhan_goc", "chan_doan_goc", "ban_goc_tieng_anh", "clin (dich)", "folk (dan gian)",
                    "tu_dan_gian", "cach_chua_dan_gian", "thay_doi_so_voi_goc", "nguon_xac_thuc_cach_chua",
                    "trang_thai_xac_thuc", "dich_dung? (ok/sua)", "dan_gian_tu_nhien? (ok/sua)",
                    "cach_chua_co_that? (ok/sua)", "ghi_chu"])
        for c in cases:
            en, lab, dx = src[c["src_id"]]
            w.writerow([c["id"], c["gold"], c["src_id"], lab, dx, en, c["clin"], c["folk"], ", ".join(c["folk_terms"]),
                        c["remedy"], c["adapt"], c["remedy_source"], c["remedy_status"], "", "", "", ""])

    no_label = [c["id"] for c in cases if not c["folk_terms"]]
    if no_label:
        print("note: folk text without a lexicon label:", " ".join(no_label))
    gold = Counter(c["gold"] for c in cases)
    print(f"{len(cases)} cases {dict(gold)} -> {len(rows)} prompts "
          f"({Counter(r['variant'] for r in rows)}); {len(term_counts)} folk terms used")


if __name__ == "__main__":
    build()
