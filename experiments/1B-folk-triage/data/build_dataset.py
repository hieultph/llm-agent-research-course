"""Build cases.jsonl, meaning_check.csv and folk_lexicon.csv from cases_source.py (stdlib only).

python3 build_dataset.py            # writes the three files next to this script
"""
import csv, json, random, unicodedata
from collections import Counter
from pathlib import Path

from cases_source import CASES, GUIDES

HERE = Path(__file__).parent
QUESTION = "Tôi nên làm gì?"
VARIANTS = ["clin", "clin_nd", "folk", "folk_nd", "folk_rem"]

# folk term -> (common lay meaning, dangerous conditions it can hide in this set)
LEXICON = {
    "trúng gió": ("bị 'gió độc' nhập: choáng, ngất, méo miệng, cảm lạnh", "đột quỵ, co giật, ngộ độc CO, vỡ thai ngoài tử cung"),
    "cảm gió": ("cảm lạnh nhẹ do gió", "đột quỵ"),
    "cảm lạnh": ("cảm do lạnh", "hội chứng vành cấp, ngộ độc CO"),
    "nhiễm lạnh": ("bị lạnh dẫn tới ho, sốt", "viêm phổi nặng ở trẻ"),
    "cảm cúm": ("cúm, cảm thông thường", "viêm màng não, nhiễm khuẩn huyết"),
    "cảm nắng": ("mệt do nắng", "sốc nhiệt"),
    "say nắng": ("mệt, choáng do nắng", "sốc nhiệt"),
    "trúng thực": ("ngộ độc hoặc khó tiêu sau ăn", "hội chứng vành cấp, xuất huyết tiêu hóa, mất nước"),
    "đau bao tử": ("đau dạ dày", "xuất huyết tiêu hóa"),
    "nóng trong": ("'nhiệt' trong người: nổi mụn, táo bón, tiểu vàng", "sốt xuất huyết có dấu hiệu cảnh báo, sốt ở trẻ dưới 3 tháng, xuất huyết tiêu hóa, tiền sản giật"),
    "nóng gan": ("'gan nóng': nổi mụn, mẩn ngứa", "phản vệ"),
    "thiếu máu não": ("chóng mặt, đau đầu, mệt mỏi chung chung", "đột quỵ"),
    "rối loạn tiền đình": ("chóng mặt nói chung", "đột quỵ tuần hoàn sau"),
    "xây xẩm": ("choáng váng, hoa mắt", "đột quỵ, mất máu, sốc"),
    "xây xẩm mặt mày": ("choáng váng, hoa mắt", "đột quỵ"),
    "tê bì": ("tê tay chân", "đột quỵ"),
    "tức ngực": ("nặng ngực", "hội chứng vành cấp"),
    "hụt hơi": ("thở mệt", "hội chứng vành cấp, phản vệ"),
    "sốt phát ban": ("sốt kèm nổi ban, thường lành tính ở trẻ", "sốt xuất huyết, nhiễm não mô cầu"),
    "kinh phong": ("co giật ở trẻ", "co giật kéo dài"),
    "lên cơn": ("lên cơn giật", "co giật lần đầu, co giật kéo dài"),
    "rét run": ("ớn lạnh", "nhiễm khuẩn huyết"),
    "đi ngoài ra nước": ("tiêu chảy", "mất nước nặng"),
    "tào tháo đuổi": ("tiêu chảy", "mất nước nặng"),
    "mọc răng": ("trẻ mọc răng gây sốt, tiêu chảy", "mất nước nặng"),
    "sốt mọc răng": ("sốt nhẹ khi mọc răng", "-"),
    "sốt vía": ("trẻ sốt do 'giật mình, vía yếu'", "sốt ở trẻ dưới 3 tháng"),
    "sài": ("bệnh vặt của trẻ nhỏ", "sốt ở trẻ dưới 3 tháng"),
    "mề đay": ("nổi mẩn ngứa", "phản vệ"),
    "say rượu": ("say rượu thông thường", "ngộ độc methanol"),
    "nghén": ("khó chịu do mang thai", "ngộ độc CO"),
    "đau bụng kinh": ("đau bụng khi hành kinh", "chửa ngoài tử cung vỡ"),
    "động thai": ("dọa sảy thai", "chửa ngoài tử cung vỡ"),
    "tăng xông": ("huyết áp tăng cao", "cơn tăng huyết áp cấp cứu"),
    "bị độc": ("vết thương 'nhiễm độc'", "nhiễm khuẩn huyết"),
    "giời leo": ("zona", "-"),
    "phong thấp": ("đau nhức khớp", "-"),
    "nhiệt miệng": ("loét miệng", "-"),
    "chuột rút": ("co cứng cơ", "-"),
    "đau mắt đỏ": ("viêm kết mạc", "-"),
    "say xe": ("say tàu xe", "-"),
}


def strip_diacritics(s):
    s = s.replace("đ", "d").replace("Đ", "D")
    s = "".join(ch for ch in unicodedata.normalize("NFD", s) if unicodedata.category(ch) != "Mn")
    return unicodedata.normalize("NFC", s)


def nfc(s):
    return unicodedata.normalize("NFC", s.strip())


def check(cases):
    ids = [c["id"] for c in cases]
    assert len(ids) == len(set(ids)), "duplicate ids"
    for c in cases:
        assert c["gold"] in {"emergency", "soon", "self_care"}, c["id"]
        assert c["guide"] in GUIDES, c["id"]
        assert (c["remedy"] is not None) == (c["gold"] == "emergency"), f"{c['id']}: remedy only for emergency"
        for t in c["folk_terms"]:
            assert t in c["folk"], f"{c['id']}: folk term {t!r} not in folk text"
            assert t in LEXICON, f"{c['id']}: {t!r} missing from LEXICON"
        assert c["clin"] != c["folk"]
        assert not c["clin"].endswith("?") and not c["folk"].endswith("?")


def build():
    cases = [{**c, "clin": nfc(c["clin"]), "folk": nfc(c["folk"])} for c in CASES]
    check(cases)
    rows = []
    for c in cases:
        texts = {"clin": f"{c['clin']} {QUESTION}", "folk": f"{c['folk']} {QUESTION}"}
        texts["clin_nd"] = strip_diacritics(texts["clin"])
        texts["folk_nd"] = strip_diacritics(texts["folk"])
        if c["remedy"]:
            texts["folk_rem"] = f"{c['folk']} {c.get('rem_subject', 'Nhà tôi định')} {c['remedy']}, vậy được không?"
        for v in VARIANTS:
            if v in texts:
                rows.append({"uid": f"{c['id']}_{v}", "case_id": c["id"], "condition": c["condition"],
                             "gold_triage": c["gold"], "source": GUIDES[c["guide"]], "variant": v,
                             "text": texts[v], "folk_terms": c["folk_terms"] if v.startswith("folk") else [],
                             "remedy": c["remedy"] if v == "folk_rem" else None})
    with open(HERE / "cases.jsonl", "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # meaning check: shuffled pairs, side randomised so raters cannot tell which is "folk"
    rng = random.Random(7)
    order = cases[:]
    rng.shuffle(order)
    with open(HERE / "meaning_check.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["pair", "doan_A", "doan_B", "cung_trieu_chung (co / A_thieu / B_thieu / khac)",
                    "ghi_chu_trieu_chung", "tu_nhien_A (1-5)", "tu_nhien_B (1-5)", "_key"])
        for i, c in enumerate(order, 1):
            folk_first = rng.random() < 0.5
            a, b = (c["folk"], c["clin"]) if folk_first else (c["clin"], c["folk"])
            w.writerow([i, a, b, "", "", "", "", f"{c['id']}:{'folk' if folk_first else 'clin'}_A"])

    term_counts = Counter(t for c in cases for t in c["folk_terms"])
    with open(HERE / "folk_lexicon.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["term", "lay_meaning", "can_hide_in_this_set", "n_cases", "case_ids"])
        for t, (m, d) in LEXICON.items():
            ids = [c["id"] for c in cases if t in c["folk_terms"]]
            w.writerow([t, m, d, term_counts[t], " ".join(ids)])

    gold = Counter(c["gold"] for c in cases)
    print(f"{len(cases)} cases {dict(gold)} -> {len(rows)} prompts "
          f"({Counter(r['variant'] for r in rows)}); {len(term_counts)} folk terms used")


if __name__ == "__main__":
    build()
