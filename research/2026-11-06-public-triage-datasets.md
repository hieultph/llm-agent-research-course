# Bộ dữ liệu triage công khai cho 1B — 2026-11-06

**Câu hỏi:** Có bộ ca bệnh (vignette) công khai nào được bác sĩ gán nhãn mức triage, có giấy phép cho phép dịch sang tiếng Việt và dùng thay cho 72 ca tự viết?

## Nguồn
| Nguồn | Link | Rút ra | Giấy phép |
|---|---|---|---|
| Levine et al. 2024, *Lancet Digit Health* 6(8):e555–e561 | https://github.com/beamlab-hsph/gpt3-clinical-vignettes | 48 ca viết bằng lời thường, 4 mức (Emergent / 1 day / 1 week / Self-care), mỗi mức 12 ca. Được viết lại từ bộ Semigran 2015 | MIT |
| Semigran et al. 2015, *BMJ* 351:h3480 | (bài báo) | Bộ chuẩn gốc của Levine. Không dùng riêng vì trùng với Levine. 4 ca có nhãn khác Levine (DVT, sốt rét, viêm phổi, HUS) nên đã bỏ | — |
| Ramaswamy et al. 2026, *Nat Med*, doi 10.1038/s41591-026-04297-7 | https://github.com/ashwinra-code/gpt-health-eval | 30 ca, 3 bác sĩ độc lập gán nhãn A–D, có ca ranh giới (C/D 12, D 2, C 5, …) | CC0 |
| MedAsk benchmarks | https://github.com/medaks/medask-benchmarks | Dùng lại vignette Semigran, không có ca mới | — |
| RepVig (Zenodo 12805049) | https://zenodo.org/records/12805049 | Chỉ có nhãn, không có nội dung ca | — |
| CARE-Bench, MTS-Bench | (trang dự án) | Không phù hợp hoặc không tải được nội dung ca | — |

## Kết luận
- Dùng Levine (12 ca cấp cứu, 36 ca đối chứng) và Ramaswamy (2 ca D, 12 ca C/D).
- Chỉ có 14 ca cấp cứu nghiêm ngặt. Thêm 10 ca C/D làm nhóm "khẩn".
- Bỏ: các ca cần xét nghiệm mới hiểu được, các ca có ý định tự tử, ca do cây thường xuân độc (không có ở Việt Nam), và các ca Levine trùng hoặc có nhãn mâu thuẫn.
- Kết quả: 52 ca. Hieu đồng ý không tìm thêm bộ khác.

## Còn chưa chắc
- Bản dịch, bản dân gian và cách chữa dân gian do Claude viết. Hieu cần duyệt (`review_cases.csv`).
- Cần kiểm tra lại thông tin trích dẫn của Ramaswamy 2026 (tên bài, danh sách tác giả) trước khi nộp.
