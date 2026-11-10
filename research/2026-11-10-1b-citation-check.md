# Kiểm tra trích dẫn paper 1B — 2026-11-10

**Câu hỏi:** Mọi `\cite` trong `papers/1B-folk-triage/latex/main.tex` có khớp với `refs.bib` không? Metadata của từng nguồn có đúng không? Paper có mô tả đúng nội dung từng nguồn không?

Chạy bằng skill `academic-paper`, chế độ citation-check (agent citation_compliance). Kiểu trích dẫn là `splncs04` (LNCS, đánh số theo thứ tự xuất hiện).

## Truy vấn đã chạy
- Crossref API `api.crossref.org/works/<DOI>` cho 6 DOI: Semigran, Ramaswamy, Levine, Bean, Byrt, Gwet.
- Crossref `query.bibliographic` để tìm DOI cho Gourabathina, CARE-Bench và CheckList.
- arXiv API `id_list=` cho 7 bản preprint: CARE-Bench, VM14K, Overalignment, Internal Representation, VialectBench, Gorman & Pinter, Sharma.
- Tìm trên web: `MIT LLM nonclinical information typos … 7 to 9 percent Gourabathina Ghassemi`. Trang ACM chặn truy cập tự động (403), nên phải dùng nguồn này.

## Tóm tắt
| Chỉ số | Số lượng |
|---|---|
| Khóa được trích trong bài (khác nhau) | 16 |
| Mục trong refs.bib | 17 |
| Trích dẫn không có trong bib | 0 |
| Mục bib không được trích | 1 (`internalrep2026`) |
| Lỗi đã tự sửa | 7 |
| Mục cần Hieu xem lại | 3 |
| DOI đã đối chiếu trên Crossref | 9/9 nguồn có DOI, đều khớp |
| Nguồn trong 5 năm gần đây | 12/17 (71%) |

## Đã tự sửa trong refs.bib
| # | Mục | Lỗi | Sửa |
|---|---|---|---|
| 1 | semigran2015 | Thiếu DOI | Thêm `10.1136/bmj.h3480` |
| 2 | gourabathina2025medium | Thiếu DOI | Thêm `10.1145/3715275.3732121` (Crossref) |
| 3 | carebench2026 | Thiếu DOI | Thêm `10.18653/2026.aacl-long.63`. Crossref xác nhận bài in trong kỷ yếu IJCNLP-AACL 2026, tr. 1340–1363 |
| 4 | ribeiro2020checklist | Thiếu DOI; tên kỷ yếu viết tắt | Thêm `10.18653/v1/2020.acl-main.442`; ghi đầy đủ tên kỷ yếu ACL 2020 |
| 5 | bean2026reliability | Ghi "and others" dù chỉ thiếu 1 tác giả | Crossref có 11 tác giả, thêm Mahdi, Adam ở cuối |
| 6 | sharma2024sycophancy | Sai và thiếu tác giả so với arXiv | Tomek → Tomasz Korbak; thêm Newton Cheng (sau Bowman); Scott → Scott R. Johnston |
| 7 | internalrep2026 | Tiêu đề cũ (arXiv v2 đã đổi tên) | Đổi sang "Where Do Apparent LLM Clinical Triage Failures Arise? Localizing the Multiple-Choice Format Effect" |

## Cần Hieu xem lại
| # | Chỗ | Vấn đề | Gợi ý |
|---|---|---|---|
| 1 | Related Work, đoạn "Triage by symptom checkers" | Câu "LLM audits now use the same design" ngay sau câu mô tả "a three-level urgency scale". Nhưng Ramaswamy dùng 4 mức A–D (chính paper ghi vậy ở mục 3.1), CARE-Bench dùng 4 nhãn hành động, và nhãn của CARE-Bench được dựng lại từ hội thoại chứ không phải vignette do bác sĩ viết | Sửa thành kiểu "LLM audits follow the same vignette-based approach" và bỏ ý "three-level" khỏi phần được gán cho các bài này |
| 2 | `internalrep2026` | Có trong bib nhưng không được trích | Xóa khỏi bib, hoặc trích ở Discussion: bài này cho thấy định dạng trắc nghiệm làm tăng under-triage, liên quan tới việc paper chọn câu trả lời tự do |
| 3 | 5 bản preprint chưa qua bình duyệt (VM14K, Overalignment, VialectBench, Gorman & Pinter, Internal Representation) | Phản biện có thể hỏi | Không sai; nếu có bản đã đăng hội nghị thì nên thay |

## Nội dung paper so với nguồn
| Nguồn | Paper viết | Nguồn nói | Kết luận |
|---|---|---|---|
| Ramaswamy 2026 | "under-triaged about half of physician-agreed emergencies" | Abstract (Crossref): "undertriaged 52% of cases" trong các ca cấp cứu chuẩn | Khớp |
| Gourabathina 2025 | Nhiễu typo, khoảng trắng, ngôn ngữ màu mè/không chắc chắn, giới tính → "7–9% shift toward self-management" | MIT News: 7–9% tăng gợi ý tự xử lý ở nhà, trên 9 kiểu thay đổi tin nhắn | Khớp |
| Bean 2026 | LLM tự xác định đúng bệnh nhưng không giúp được người dùng | Tiêu đề và thiết kế: thử nghiệm ngẫu nhiên, có đăng ký trước | Khớp (theo ghi chép research trước) |
| CARE-Bench | Đánh giá phân loại khi bệnh nhân kể dần qua hội thoại | Abstract: "sequential patient-facing triage … patient-disclosure prefixes" | Khớp |
| Sharma 2024 | LLM có xu hướng đồng ý với quan điểm người dùng | Abstract | Khớp |
| Overalignment 2026 | Sycophancy cả trong bối cảnh y khoa | Abstract: medical MCQA, Adjusted Sycophancy Score | Khớp |
| VM14K | Benchmark trắc nghiệm kiến thức y khoa | 14.000 câu trắc nghiệm, 34 chuyên khoa | Khớp |
| Gorman & Pinter | Bỏ dấu khi tiền xử lý làm hại hệ thống NLP | Abstract: "adverse effects … removing diacritics" | Khớp |
| VialectBench | 6 nhóm phương ngữ, không model nào miễn nhiễm | Abstract (xem research note 2026-11-10) | Khớp |
| Semigran 2015 | Vignette do bác sĩ gán nhãn, thang 3 mức, báo cáo under-triage và over-triage riêng | Bài kiểm tra symptom checker: emergent / non-emergent / self-care | Khớp |

## Đã xử lý sau báo cáo (Hieu đồng ý sửa)
- Mục 1: câu trong Related Work đổi thành "LLM triage audits follow the same vignette-based approach, with finer urgency scales".
- Mục 2: xóa `internalrep2026` khỏi refs.bib. Thông tin của bài vẫn còn trong báo cáo này nếu sau cần trích.
- Ramaswamy 30 hay 60: file công bố `ramaswamy2026_vignettes.csv` có đúng 30 scenario, nên paper ghi "30 symptoms-only scenarios" là đúng. Con số 60 vignette trong abstract của họ tính trên toàn bộ thiết kế thí nghiệm.

## Còn chưa chắc
- Chưa đọc được abstract gốc của Gourabathina trên ACM (bị chặn 403). Con số 7–9% lấy từ MIT News.
- Chưa kiểm tra Retraction Watch. Không có dấu hiệu bài nào bị rút: các trang Crossref và arXiv không ghi chú rút bài.
- Ramaswamy có 19 tác giả. Bib ghi 10 tác giả + "others", LNCS chấp nhận cách này. Danh sách đủ có trên Crossref nếu cần.

## Nguồn
- Crossref REST API: https://api.crossref.org
- arXiv API: https://export.arxiv.org/api/query
- MIT News, "LLMs factor in unrelated information when recommending medical treatments" (2025-06-23): https://news.mit.edu/2025/llms-factor-unrelated-information-when-recommending-medical-treatments-0623
- Medical Economics: https://www.medicaleconomics.com/view/even-a-small-typo-can-throw-off-ai-medical-advice-mit-study-says
