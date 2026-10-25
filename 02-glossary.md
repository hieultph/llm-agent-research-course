# Master Glossary — English ↔ Vietnamese

> [!summary] Tóm tắt (VI)
> Bảng thuật ngữ tổng, xếp theo chặng. Cột "Ghi chú" giải thích bằng tiếng Việt đời thường.
> Nhiều thuật ngữ giới nghiên cứu Việt Nam vẫn giữ nguyên tiếng Anh (ví dụ "token", "embedding"). Khi viết báo luôn dùng tiếng Anh, nhưng hiểu nghĩa bằng tiếng Việt sẽ nhớ lâu hơn.
> Mỗi chặng mới sẽ bổ sung thêm thuật ngữ vào đây.

## Phase 0 — Foundations

| English | Tiếng Việt | Ghi chú |
|---|---|---|
| variable | biến | Cái hộp có tên để chứa giá trị |
| list / dictionary | danh sách / từ điển | `[1,2,3]` / `{"tên": "giá trị"}` |
| function | hàm | Một đoạn code có tên, nhận đầu vào, trả đầu ra |
| loop | vòng lặp | Lặp lại một việc nhiều lần |
| class / object | lớp / đối tượng | Khuôn mẫu / thứ được tạo ra từ khuôn mẫu |
| package / library | gói / thư viện | Code người khác viết sẵn, cài bằng `pip` |
| JSON | JSON | Định dạng văn bản để lưu dữ liệu có cấu trúc, dùng khắp nơi trong LLM |
| array | mảng | Danh sách số mà NumPy tính toán rất nhanh |
| scalar | vô hướng | Một con số đơn lẻ |
| vector | vectơ | Danh sách số; cũng là một mũi tên có hướng và độ dài |
| dimension | chiều | Số lượng con số trong một vectơ |
| dot product | tích vô hướng | Nhân từng cặp rồi cộng lại |
| norm (length) | chuẩn (độ dài) | Độ dài của mũi tên |
| cosine similarity | độ tương đồng cosin | Hai mũi tên cùng hướng đến mức nào, từ −1 đến 1 |
| embedding | vectơ nhúng (embedding) | Biến chữ thành vectơ sao cho nghĩa gần thì vectơ gần |
| matrix | ma trận | Bảng số có hàng và cột |
| shape | kích thước (shape) | Số hàng × số cột, ví dụ (3, 4) |
| transpose | chuyển vị | Đổi hàng thành cột |
| matrix multiplication | phép nhân ma trận | Mỗi ô kết quả là tích vô hướng của một hàng với một cột |
| probability | xác suất | Khả năng xảy ra, từ 0 đến 1 |
| distribution | phân phối | Danh sách xác suất cho mọi kết quả, cộng lại bằng 1 |
| logit | logit (điểm thô) | Điểm số trước khi đổi thành xác suất |
| softmax | softmax | Hàm biến điểm thô thành xác suất |
| temperature | nhiệt độ | Núm vặn độ "liều" khi chọn chữ tiếp theo |
| logarithm (log) | lôgarit | Phép ngược của lũy thừa; biến phép nhân thành phép cộng |
| loss | hàm mất mát | Con số đo mô hình sai bao nhiêu; càng nhỏ càng tốt |
| cross-entropy | entropy chéo | Hàm mất mát chuẩn cho bài toán đoán chữ tiếp theo |
| derivative | đạo hàm | Độ dốc của đường cong tại một điểm |
| gradient | gradient (vectơ độ dốc) | Đạo hàm theo nhiều biến cùng lúc; chỉ hướng dốc lên |
| gradient descent | hạ gradient | Đi ngược hướng dốc để giảm mất mát |
| learning rate | tốc độ học | Kích thước mỗi bước đi |
| parameter / weight | tham số / trọng số | Các con số mô hình tự điều chỉnh khi học |
| training | huấn luyện | Lặp đi lặp lại: đoán, đo sai, sửa trọng số |
| epoch | epoch (vòng huấn luyện) | Mô hình xem hết dữ liệu một lần |
| tensor | tensor | Mảng nhiều chiều trong PyTorch, chạy được trên GPU |
| autograd | tự động tính đạo hàm | PyTorch tự tính gradient giúp bạn |
| GPU / CUDA | GPU / CUDA | Card đồ họa / nền tảng để chạy tính toán trên card NVIDIA |
| token | token | Mảnh chữ mà mô hình đọc, có thể là một từ, một phần từ hoặc một ký tự |
| prompt | câu lệnh đầu vào (prompt) | Văn bản bạn đưa cho mô hình |
| inference | suy luận (chạy mô hình) | Dùng mô hình đã huấn luyện để sinh kết quả |
| abstract | tóm tắt bài báo | Đoạn đầu bài báo |
| related work | các nghiên cứu liên quan | Phần so sánh với bài đã có |
| baseline | phương pháp đối chứng | Cách làm có sẵn để so sánh |
| ablation study | thí nghiệm loại bỏ thành phần | Bỏ từng phần để xem phần nào thật sự có ích |
| benchmark | bộ đánh giá chuẩn | Bộ dữ liệu + cách chấm điểm mà nhiều người cùng dùng |
| peer review | phản biện | Chuyên gia đọc và chấm bài trước khi đăng |
| semantic search | tìm kiếm theo ngữ nghĩa | Tìm theo nghĩa thay vì khớp từng chữ |

## Phase 1 — Transformers (preview, completed when Phase 1 is written)

| English | Tiếng Việt | Ghi chú |
|---|---|---|
| neural network | mạng nơ-ron | Nhiều lớp phép nhân ma trận + hàm phi tuyến |
| activation function | hàm kích hoạt | Phần "bẻ cong" giúp mạng học được quan hệ phức tạp |
| tokenizer | bộ tách token | Cắt văn bản thành token |
| BPE (byte-pair encoding) | mã hóa cặp byte | Cách tạo bộ từ vựng bằng cách gộp dần các cặp ký tự hay đi cùng nhau |
| fertility | độ phân mảnh | Trung bình một từ bị cắt thành bao nhiêu token |
| attention | cơ chế chú ý | Mỗi token tự quyết định nên "nhìn" vào token nào khác |
| query / key / value | truy vấn / khóa / giá trị | Ba vai trò của mỗi token trong attention |
| transformer | transformer | Kiến trúc mạng đứng sau mọi LLM hiện nay |
| perplexity | độ bối rối | Mô hình "bất ngờ" đến mức nào với văn bản; càng thấp càng tốt |
| diacritics | dấu (thanh dấu, dấu phụ) | Dấu sắc, huyền, hỏi, ngã, nặng và dấu mũ, móc |

## Phase 2–4 terms

Added when those phases are written: RAG, retriever, reranker, LoRA, quantization, LLM-as-a-judge, function calling, ReAct, MCP, calibration, prompt injection, reward, policy, DPO, GRPO…
