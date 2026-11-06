# SOUL — người dùng là ai và làm việc thế nào

> Claude tự cập nhật file này khi suy ra được điều mới. Mỗi dòng ghi kèm *(bằng chứng, ngày)*. Điều gì sai thì sửa, không chỉ thêm.
> Bạn (Hieu) cứ sửa trực tiếp: điều bạn tự viết luôn được ưu tiên hơn điều Claude suy luận.

## Mục tiêu
- Tự học về LLM và agent theo lộ trình trong repo (phase 0–4), rồi biến thành paper thật để nộp hội nghị. *(cấu trúc repo, 00-roadmap.md)*
- Paper đang làm:
  - **1A**: dấu tiếng Việt, IEEE;
  - **1B**: folk-triage, Springer LNCS, hội nghị Q3, sprint 5 ngày từ 2026-11-05. *(2026-11-05)*
- Hướng nghiên cứu: độ tin cậy và an toàn của LLM với người dùng tiếng Việt (gõ không dấu, cách nói dân gian). *(1A, 1B)*

## Ràng buộc
- Chạy trên **Colab** (có Colab Pro, GPU A100/L4): Claude viết notebook, Hieu bấm chạy rồi gửi kết quả lại. *(2026-11-05)*
- Không có chuyên gia y khoa. Chỉ Hieu và 1 người bạn làm phần kiểm tra nghĩa và gán nhãn. *(2026-11-05)*
- Ngân sách API có hạn: dùng Gemini qua key Vertex/Agent Platform, credit trả trước. *(2026-11-06)*

## Giá trị và tiêu chuẩn
- **Dữ liệu phải đứng vững trước phản biện**: không dùng dữ liệu LLM tự bịa. Ưu tiên bộ công khai có nhãn của bác sĩ, kể cả khi số ca ít hơn. *(yêu cầu thay 72 ca tự viết bằng bộ công khai, 2026-11-06)*
- **Muốn duyệt trước khi dùng**: phần dịch, chuyển thể và các thay đổi lớn phải gửi Hieu xem trước. *(2026-11-06)*
- Chấp nhận đánh đổi hợp lý khi được giải thích rõ lý do. Hỏi lại khi con số trông lạ ("sao 52 mà chỉ lấy 14?"), rồi quyết nhanh ("đủ rồi"). *(2026-11-06)*
- Muốn Claude research từ nguồn trước khi đề xuất, và lưu lại quá trình. *(2026-11-06)*
- Thích có nhật ký làm việc và tài liệu rõ ràng để nhìn lại. *(yêu cầu tạo JOURNAL, 2026-11-06)*

## Cách giao tiếp
- Viết tiếng Việt, ngắn gọn, thân mật. Thường gửi tin nhắn ngắn và có thể có lỗi gõ. *(toàn bộ hội thoại)*
- Thích câu trả lời có bảng, con số cụ thể, và biết bước tiếp theo bạn ấy cần làm gì.
- Tự thử trước (tạo key, đọc hướng dẫn trên mạng) rồi nhờ Claude kiểm tra. *(thử API key, 2026-11-06)*

## Thói quen kỹ thuật
- Máy local: Linux, có `uv` và miniconda. Repo lưu trên GitHub (`hieultph/llm-agent-research-course`). Chưa cài `gh` CLI.
- Kết quả trên Colab lưu ở `MyDrive/llm-research/<thí-nghiệm>/`.

## Còn chưa biết (hỏi khi cần)
- Tên hội nghị Q3 cụ thể và hạn nộp chính xác.
- Trình độ chuyên môn (sinh viên? đang đi làm?) và mục tiêu dài hạn (học cao học? xin việc nghiên cứu?).
