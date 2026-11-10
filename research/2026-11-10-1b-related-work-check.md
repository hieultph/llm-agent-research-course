# Rà soát related work cho paper 1B — 2026-11-10

**Câu hỏi:** Đã có công trình nào đo LLM với câu hỏi sức khỏe tiếng Việt kiểu người thường, từ dân gian hoặc gõ không dấu chưa? Câu trả lời quyết định câu "we are not aware of…" và mục Related Work.

## Truy vấn đã chạy
- `Vietnamese medical LLM benchmark lay language health questions 2026` (web, extended) → VM14K, VietMed-MCQ, ViMedCSS (giọng nói), nghiên cứu về tính nhất quán đa ngôn ngữ. Không có bộ nào dùng câu hỏi kiểu người thường.
- `LLM robustness Vietnamese without diacritics unaccented input evaluation` (web) → VialectBench (độ bền với phương ngữ), "Don't Touch My Diacritics", ViLLM-Eval/Crossing Linguistic Horizons (độ bền với lỗi gõ). Không có công trình nào đo LLM với input không dấu.
- `folk illness terms cultural idioms of distress LLM medical triage evaluation` (web) → chỉ có tài liệu nhân học về *cultural concepts of distress* (DSM-5-TR). Không có công trình đánh giá LLM.

## Nguồn
| Nguồn | Link | Đã đọc gì | Rút ra | Giấy phép / độ tin cậy |
|---|---|---|---|---|
| Tran et al. 2026, *How Robust Are LLMs to Vietnamese Dialects?* | https://arxiv.org/abs/2608.10414 | Abstract | 2.400 câu viết lại theo 6 nhóm phương ngữ. Trên 10 model, điểm trung bình giảm 2,82%, không model nào miễn nhiễm. Gần nhất với 1B: cùng là biến đổi bề mặt giữ nguyên nghĩa, nhưng không thuộc lĩnh vực y tế và không xét mất dấu | Preprint, chưa có nơi công bố |
| Gorman & Pinter 2024, *Don't Touch My Diacritics* | https://arxiv.org/abs/2410.24140 | Abstract | Bài quan điểm: bỏ dấu khi tiền xử lý làm hại hiệu năng và sự công bằng giữa các ngôn ngữ. Không có số liệu | Preprint, 6 trang |
| Bui et al. 2026, *Perspectives on Cross-Lingual Consistency in LLMs for Medical Questions* | https://arxiv.org/abs/2609.07687 | Abstract | Tổng quan và khảo sát 356 người về việc câu trả lời y tế nên nhất quán hay thích nghi theo văn hóa. Chỉ liên quan gián tiếp | EMNLP 2026 Main |
| VietMed-MCQ (Huynh et al. 2026) | https://arxiv.org/abs/2601.03792 | Trang abstract | **Đã bị rút** (v2, 10/06/2026). Không trích dẫn | Đã rút |
| VM14K | https://arxiv.org/abs/2506.01305 | Đã dùng trước đó | Bộ trắc nghiệm kiến thức y khoa | Đã có trong refs.bib, đã có đủ tác giả (Nguyen et al. 2025) |

## Kết luận
- Vẫn giữ được câu "we are not aware of work that measures lay phrasing, folk-illness terms or missing diacritics in Vietnamese health questions", vì không tìm thấy công trình nào làm việc này.
- Thêm VialectBench vào mục độ bền: công trình tiếng Việt gần nhất, nhưng không về y tế và không xét mất dấu.
- Thêm Gorman & Pinter để làm rõ vì sao mất dấu là vấn đề.
- Không trích VietMed-MCQ vì bài đã bị rút.

## Còn chưa chắc
- Mới đọc abstract, chưa đọc toàn văn VialectBench để xem họ có dùng câu không dấu như một biến thể hay không.
- Tìm kiếm chỉ trên web. Chưa tìm trên ACL Anthology và Google Scholar riêng, nên có thể sót bài hội nghị năm 2026.
