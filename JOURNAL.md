# Journal

Nhật ký làm việc, mục mới nhất ở trên. Định dạng và quy tắc: xem [CLAUDE.md](CLAUDE.md#2-journal).

---

## 2026-11-08 — 1B: cập nhật phân tích, notebook và paper theo bộ dữ liệu mới

**Vấn đề**
- Bộ dữ liệu đã đổi sang 52 ca công khai, chia 4 nhóm (cấp cứu / khẩn / cần đi khám / tự chăm sóc), có folk_rem cho cả 52 ca. Code phân tích và paper vẫn viết cho 72 ca tự viết cũ.

**Đã làm / giải pháp**
- `ft.py`:
  - nhóm khẩn: cột `under_u` = trả lời self_care hoặc none;
  - `contrast_table` và `pooled_contrasts` có thêm tham số `gold=` (cấp cứu là kết quả chính, khẩn là kết quả phụ), mỗi nhóm hiệu chỉnh Holm riêng;
  - nhóm đối chứng = soon + self_care;
  - `remedy_table` tính theo model × nhóm, có tùy chọn `sourced_only`;
  - thêm `remedy_sensitivity`: so tất cả ca với 24 ca có nguồn;
  - `unsafe_endorse` chỉ tính trên ca cấp cứu và khẩn.
- `make_notebooks.py`: sửa phần mô tả (260 câu hỏi, nguồn dữ liệu); bước 5–6 xuất thêm `contrasts_urgent`, `pooled_urgent`, `remedy_sensitivity`; `summary.json` có thêm phần khẩn và phân tích độ nhạy. Đã sinh lại 2 notebook.
- Paper:
  - viết lại abstract, contribution 1, toàn bộ phần Dataset (nguồn, ánh xạ nhãn, ca bị loại, 5 phiên bản, nguồn của cách chữa, ai soạn và ai duyệt), ví dụ E08, bảng dữ liệu, Measures, Statistics, Limitations, Ethics;
  - bib: thêm `levine2024gpt3`; sửa `ramaswamy2026chatgpthealth` (đã đối chiếu với Crossref); bỏ 6 trích dẫn hướng dẫn điều trị không còn dùng.
- Xóa `data/cases_source.py`, sửa README. Thêm `requirements.txt` (pandas, numpy, matplotlib, requests, scipy) và `.venv` cho thí nghiệm này.

**Kết quả**
- Chạy thử trên dữ liệu giả (3 model, 1 model có thêm m1), dùng `.venv`: `build_frame`, mọi bảng, 3 hình, phiếu chấm tay và bước 5–6 của notebook B đều chạy hết, ra đủ 13 file bảng.
- Chưa biên dịch được LaTeX vì máy không có TeX. Đã kiểm tra số ngoặc và cặp begin/end khớp nhau.

**Còn lại / bước tiếp**
- Đã commit và push lên `origin main` (chỉ phần 1B, JOURNAL, SOUL; không gồm file 1A).
- Gửi `meaning_check.csv` mới (52 cặp, nhớ xóa cột `_key`) cho 2 người kiểm tra nghĩa.
- Chạy notebook A và B.

## 2026-11-08 — 1B: đọc bản dataset Hieu đã duyệt

**Vấn đề**
- Hieu đã duyệt 52 ca trên Drive (`1B_llm_benchmark_dataset_reviewed`, có bản .csv và bản Sheet, nội dung giống nhau). Claude kiểm tra lại xem bản này dùng được chưa.

**Đã làm / giải pháp**
- Tải về, so từng chữ với `review_cases.csv`.
- Mở từng link nguồn (24 link) và kiểm tra trong trang có nhắc đến các thành phần của cách chữa không.

**Kết quả**
- Phần duyệt:
  - dịch đúng: 52/52 ok;
  - cách nói dân gian tự nhiên: 52/52 ok;
  - cách chữa có nguồn một phần: 24 ca; chưa xác minh: 28 ca.
- Hieu đã thêm:
  - cách chữa dân gian cho cả 28 ca nhẹ (trước chỉ có ở ca cấp cứu và khẩn);
  - 4 cột mới: `prompt_folk_kem_cach_chua`, `nguon_xac_thuc_cach_chua`, `pham_vi_xac_thuc_nguon`, `trang_thai_xac_thuc`.
- Link nguồn:
  - 22/24 mở được và đúng chủ đề;
  - N02 và N09 bị Cloudflare chặn, không kiểm tra được;
  - trang nguồn không nhắc đến: "cạo gió" (E03), "kiêng gió" (E07), "mã đề" (S06), "óc heo, ngải cứu" (S09).
- Lỗi cần sửa:
  - S02: cụm "có mảng trắng" bị lặp lại.
  - E06: bản dân gian thêm triệu chứng "tê" không có trong bản gốc.
  - E14, U03: bản dân gian gợi ý nguyên nhân y khoa ("đường huyết tăng", "do thuốc huyết áp").
  - Danh sách từ dân gian cần cập nhật theo các từ mới.

**Quyết định của Hieu:**
- S02: Hieu đã tự sửa trên Sheet.
- E06: giữ nguyên chữ "tê" vì nghe tự nhiên hơn.
- E14, U03 và lexicon: nhờ Claude sửa.

**Đưa bản duyệt vào code**
- Lưu bản duyệt cuối (Sheet, sửa lúc 19:05) vào [data/review/cases_reviewed_2026-11-08.csv](experiments/1B-folk-triage/data/review/cases_reviewed_2026-11-08.csv).
- Tạo lại `CASES` và `LEXICON` trong `cases_public.py` từ bản duyệt.
  - Thêm 2 trường `remedy_source` và `remedy_status`.
  - Bỏ trường `rem_subject`.
- Sửa bản dân gian:
  - E14: "…chắc người bị nóng trong";
  - U03: "…chắc bị cảm".
- Lexicon có 34 từ.
  - Thêm: tích nước, thiếu máu lên não, máu huyết không lưu thông (E06), say cà phê, viêm phụ khoa.
  - Bỏ vì là từ chỉ triệu chứng hoặc nguyên nhân thật, không phải nhãn dân gian: sưng phù, khí hư, côn trùng cắn, nọc ong, bị trĩ.
  - Bỏ 2 từ không còn ca nào dùng: phù thũng, rối loạn tiền đình.
  - "nặng ngực" không xuất hiện trong bản dân gian của S12 nên không tính.
- Sửa `build_dataset.py`:
  - ca nào cũng có cách chữa;
  - prompt folk_rem theo mẫu của Hieu: "Tôi tính …, như vậy có được không?";
  - thêm `remedy_status` vào `cases.jsonl`.

**Kết quả**
- 52 ca → 260 prompt (5 biến thể × 52).
- folk_rem khớp từng chữ với cột `prompt_folk_kem_cach_chua` của Hieu, trừ E14 và U03 vừa sửa.
- Có nguồn / chưa xác minh theo nhóm: cấp cứu 7/7, khẩn 3/7, cần đi khám 7/8, tự chăm sóc 7/6.
- Còn 2 ca chưa có nhãn dân gian: S12, N06.
- Drive: đã upload "1B review_cases v2" và "1B folk_lexicon v2". Lexicon cũ đã chuyển vào thùng rác.

**Còn lại / bước tiếp**
- Quyết định nhãn dân gian cho S12 và N06.
- `ft.py`: thêm nhóm khẩn; folk_rem cho cả 52 ca (đo việc khuyên ngăn cách chữa ở ca nhẹ để làm đối chứng); phân tích phụ trên các ca có nguồn.
- Notebook, paper (phần Dataset, bib), xóa `cases_source.py`, rồi commit.

## 2026-11-07 — 1B: đưa dataset lên Google Drive để duyệt

**Vấn đề**
- Hieu muốn duyệt và sửa bộ 52 ca trực tiếp trên Google Drive.
- `gog` (Google CLI) báo `invalid_grant`, vì token lưu từ 2026-03-17 đã hết hạn.

**Đã làm / giải pháp**
- Chạy lại `gog auth add hieultph@gmail.com --services drive,sheets,docs --force-consent`. Hieu bấm cho phép.
- Tạo `My Drive/llm-research/1B-folk-triage/dataset-review/` ([folder](https://drive.google.com/drive/folders/1WIY-Lh-pE4zBNK--BgJ3JcXE0Z24hxc-)).
- Upload `review_cases.csv` dưới dạng Google Sheet ([1B review_cases (duyệt)](https://docs.google.com/spreadsheets/d/1485RlO2nUcVEizuQMTvheiIbgGNf1FnAmOCa9hShtYA/edit)).
- Upload `folk_lexicon.csv` dưới dạng Google Sheet. Bỏ 4 file trong `sources/` (dữ liệu gốc và giấy phép) vào thư mục con `sources/`.

**Kết quả**
- Tải Sheet về kiểm tra lại: đủ 52 dòng, tiếng Việt hiển thị đúng.

**Còn lại / bước tiếp**
- Hieu duyệt trên Sheet. Sau đó Claude tải về (`gog drive download 1485RlO2… --format csv`), cập nhật `cases_public.py` theo ghi chú, rồi build lại.

## 2026-11-06 — 1B: chuyển sang dữ liệu công khai, thiết lập rule làm việc

**Vấn đề**
- Bộ 72 ca của 1B do Claude tự viết dựa theo hướng dẫn điều trị. Hieu không muốn dùng dữ liệu do LLM bịa trong paper.
- API key Gemini không chạy:
  - key `AIza…`: Vertex trả về 401, AI Studio trả về 402 vì hết credit trả trước;
  - với key Vertex: Gemma 4 trả về 404 trên Vertex.

**Đã làm / giải pháp**
- Chuyển sang key Google Cloud Agent Platform (`AQ.…`). `ft.py` tự nhận ra loại key và gọi endpoint Vertex. Bỏ Gemma 4 khỏi danh sách API model (commit `152124b`).
- Tìm dữ liệu công khai (chi tiết: [research/2026-11-06-public-triage-datasets.md](research/2026-11-06-public-triage-datasets.md)):
  - **Levine et al. 2024**: 48 ca, giấy phép MIT;
  - **Ramaswamy et al. 2026**: 30 ca, giấy phép CC0.
- Chọn 52 ca, giữ nguyên nhãn gốc: 14 cấp cứu, 10 khẩn (C/D), 15 cần đi khám, 13 tự chăm sóc. Claude dịch, viết bản dân gian và cách chữa dân gian, trong `data/cases_public.py`.
- Tạo `CLAUDE.md`, `SOUL.md`, `JOURNAL.md` và `research/`.

**Kết quả**
- Bản build: 52 ca, 232 prompt, 31 từ dân gian. Bản để duyệt: `experiments/1B-folk-triage/data/review_cases.csv`.
- Hieu chốt giữ 14 ca cấp cứu và 10 ca khẩn, không tìm thêm bộ khác.
- Chưa commit thay đổi dữ liệu.

**Còn lại / bước tiếp**
- Hieu duyệt `review_cases.csv`.
- Sau khi duyệt: thêm nhóm khẩn vào `ft.py`, sửa notebook, sửa phần Dataset và bib của paper, xóa `cases_source.py`, rồi commit.
- Hieu đặt key vào Colab Secrets (`GOOGLE_API_KEY`) và đổi key mới, vì key cũ đã lộ trong chat.
