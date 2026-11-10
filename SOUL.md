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
- Duyệt kỹ và chủ động mở rộng: tự thêm cột nguồn, phạm vi xác thực và trạng thái xác thực; thêm cách chữa dân gian cho cả ca nhẹ; ghi rõ là nguồn chỉ xác nhận một phần, không phải xác nhận hiệu quả. *(bản duyệt 1B, 2026-11-08)*
- Bản lâm sàng phải sát bản dịch từ ca gốc: chỉ viết lại cho tự nhiên, không thêm hay bớt thông tin. Khi hai bản lệch nhau thì sửa bản dân gian. *(góp ý cho vòng kiểm tra nghĩa, 2026-11-08)*
- Không nhận mọi góp ý của người duyệt: chỉ sửa chỗ thật sự đổi dữ kiện hoặc mức độ. Bản dân gian phải giữ cách nói người Việt hay dùng, dù nghe hơi khác bản lâm sàng; ví dụ "ăn không thấy ngon" = "ăn kém". Muốn xem gợi ý trước rồi mới sửa. *(phản hồi về vòng chấm mù, 2026-11-08)*
- Thực tế về nguồn lực người duyệt: muốn giảm khâu kiểm tra bằng người ngoài khi có thể. Người bạn hỗ trợ có dùng AI. Chấp nhận làm thêm một vòng chấm mù khi được giải thích lý do. *(2026-11-08)*
- Lỗi do mình cài đặt (ví dụ giới hạn token quá nhỏ) thì chạy lại cho đủ, không loại dữ liệu cho nhanh. *(câu trả lời bị cắt ở 512 token, 2026-11-09)*
- Muốn Claude research từ nguồn trước khi đề xuất, và lưu lại quá trình. *(2026-11-06)*
- Thích có nhật ký làm việc và tài liệu rõ ràng để nhìn lại. *(yêu cầu tạo JOURNAL, 2026-11-06)*

- Với review, sửa theo mức đầu tư của hội nghị: hội nghị Q3 thì chọn hướng sửa ít thay đổi nhất. Ưu tiên viết lại câu, thu hẹp khẳng định, ghi vào Limitations; không làm thêm thí nghiệm. Có quan điểm riêng về điểm mới của bài (cách nói dân gian) và phản bác góp ý mình thấy thừa, nhưng chấp nhận khi được nêu lý do cụ thể. Không có bác sĩ để nhờ kiểm tra. *(sửa paper 1B theo review, 2026-11-10)*
- Ở vòng review thứ 2, Hieu giao cho Claude tự chọn: nhận góp ý nào làm bài rõ ràng, mạnh hơn, và mạnh dạn từ chối góp ý nào có lý do hợp lý. Phân tích lại trên dữ liệu đã có thì được làm; thí nghiệm mới thì vẫn không. Hieu muốn paper có nhiều hình để người đọc dễ theo dõi. *(review vòng 2 paper 1B, 2026-11-10)*
- Hay tự gộp hoặc dọn file dữ liệu cho gọn, ví dụ gộp hai file nhãn giống nhau thành một. Khi gửi file chấm, nhắc giữ bản gốc của từng người. Thẳng thắn nhận khi mình làm sai. *(gộp nhãn hai người chấm, 2026-11-10)*

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
