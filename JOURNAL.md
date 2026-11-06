# Journal

Nhật ký làm việc, mục mới nhất ở trên. Định dạng và quy tắc: xem [CLAUDE.md](CLAUDE.md#2-journal).

---

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
