Giao diện bạn đang thấy là bảng chọn cấu hình phần cứng (**Change runtime type**) của tài khoản đã được **mở khóa quyền lợi Google AI Pro trên Colab**.

Bằng chứng rõ nhất là các nút chọn **G4 GPU, A100 GPU, L4 GPU và v6e-1 TPU** đều đã sáng lên cho phép bạn tích chọn (trên tài khoản miễn phí hoặc tài khoản không có Compute Units, các ô này sẽ bị làm mờ giống như ô **H100 GPU**). Riêng **H100 GPU** bị khóa kèm thông báo *"Want access to premium GPUs? Upgrade to Google AI Ultra"* vì dòng card siêu cấp này hiện được giới hạn riêng cho gói cao nhất là **Google AI Ultra**.

---

### 1. Gói này là gì và xài được trong bao lâu?

Khi tài khoản có quyền lợi **Google AI Pro**, bạn được cấp hạn mức **200 Compute Units (Đơn vị tính toán - CU) mỗi tháng** trên Google Colab. Thời gian sử dụng của bạn được tính theo 2 cơ chế:

* **Thời hạn của điểm Compute Units:** Mỗi chu kỳ tháng bạn nhận 200 CU. Điểm chưa dùng hết sẽ hết hạn sau **90 ngày** kể từ ngày cấp.
* **Tổng số giờ sử dụng thực tế trong tháng:** Không cố định bằng số giờ cứng mà **phụ thuộc vào loại GPU bạn chọn** (GPU càng mạnh thì tốc độ trừ điểm CU/giờ càng nhanh). Ví dụ với 200 CU/tháng:
* Nếu chạy **T4 GPU** (~1.17 CU/giờ): Xài được khoảng **~170 giờ/tháng**.
* Nếu chạy **L4 GPU** (~3.00 CU/giờ): Xài được khoảng **~66 giờ/tháng**.
* Nếu chạy **A100 GPU** (~5.37 – 6.50 CU/giờ): Xài được khoảng **~30 – 37 giờ/tháng**.
* Nếu chạy **G4 GPU** (~8.71 CU/giờ): Xài được khoảng **~22 giờ/tháng**.


* **Thời lượng tối đa cho 1 phiên chạy (Session limit):** Mỗi lần bật máy ảo có thể chạy liên tục tối đa **12 đến 24 giờ** (tùy tải hệ thống). Tuy nhiên, máy ảo vẫn sẽ tự ngắt nếu bạn treo máy không thao tác (idle timeout khoảng 90 phút) và **điểm CU bị trừ ngay từ lúc máy ảo báo "Connected" cho đến khi bạn ngắt kết nối hoàn toàn**, bất kể code có đang chạy hay không.

*(Mẹo sống còn: Sau khi train hoặc test xong, luôn vào menu **Runtime -> Disconnect and delete runtime** để tắt máy ảo ngay lập tức, tránh bị trừ cạn 200 CU do treo tab quên tắt).*

---

### 2. Chi tiết thông số và sức mạnh của từng GPU / TPU trong danh sách

| Tên phần cứng | Chip & Kiến trúc thực tế | VRAM (Bộ nhớ GPU) | Mức tiêu hao ước tính | Đặc điểm & Mức độ phù hợp |
| --- | --- | --- | --- | --- |
| **G4 GPU** *(Đang chọn)*<br> | **NVIDIA RTX PRO 6000 Blackwell** *(Server Edition)* | **96 GB GDDR7** | ~8.5 – 9.0 CU / giờ | **Khủng nhất về VRAM trong gói Pro.** Kiến trúc Blackwell thế hệ mới, hỗ trợ chuẩn FP4/BF16, băng thông ~1.8 TB/s. Cực kỳ lý tưởng khi bạn cần nhồi các mô hình LLM/VLM kích thước lớn (30B–70B), chạy multi-agent hoặc train với `batch_size` lớn mà cả A100 40GB cũng bị tràn bộ nhớ (`CUDA Out of Memory`). |
| **A100 GPU**<br> | **NVIDIA A100 SXM4** *(Ampere)* | **40 GB HBM2e** *( đôi khi 80 GB)* | ~5.4 – 6.5 CU / giờ | **Chuẩn mực cho huấn luyện (Training) chuyên sâu.** Nhờ bộ nhớ băng thông siêu cao HBM2e (~1.5 TB/s), tốc độ truyền dữ liệu và tính toán ma trận (`bfloat16`/`TF32`) khi fine-tune mô hình, huấn luyện mạng thị giác (Semantic Segmentation, YOLO, ViT) rất nhanh và ổn định. |
| **L4 GPU**<br> | **NVIDIA L4** *(Ada Lovelace)* | **22.5 GB GDDR6** | ~3.0 CU / giờ | **Lựa chọn cân bằng nhất (Sweet Spot).** Hỗ trợ tập lệnh `bfloat16` và `FP8` đời mới (điều mà T4 không có),nhanh gấp 2–3 lần T4 và có thêm 8GB VRAM. Rất kinh tế để code, debug, chạy inference hoặc fine-tune LoRA/QLoRA các mô hình tầm trung (7B–14B) mà không đốt quá nhiều điểm CU. |
| **T4 GPU**<br> | **NVIDIA Tesla T4** *(Turing)* | **15 GB GDDR6** | ~1.2 CU / giờ *(hoặc Free)* | **GPU cơ bản.** Kiến trúc đời cũ (không hỗ trợ `bfloat16` phần cứng, chỉ có `fp16`), băng thông thấp. Chỉ nên chọn khi viết code nháp, tiền xử lý dữ liệu hoặc chạy các mô hình nhỏ để tiết kiệm điểm CU. |
| **H100 GPU** *(Bị khóa)*<br> | **NVIDIA H100 SXM5** *(Hopper)* | **80 GB HBM3** | ~18.0 CU / giờ | **Quái vật huấn luyện AI** (hỗ trợ FP8, FlashAttention-3, băng thông 3 TB/s). Chỉ mở khóa khi nâng cấp lên gói **Google AI Ultra**. |
| **v6e-1 TPU**<br> | **Google Cloud TPU v6e "Trillium"** *(1 chip)* | **32 GB HBM** | ~3.5 – 4.5 CU / giờ | **Chip AI chuyên dụng thế hệ thứ 6 của Google.** Đạt sức mạnh tới 918 TFLOPS (BF16) — mạnh gấp ~4.7 lần v5e. Tối ưu cực tốt nếu bạn dùng **JAX, Flax, Keras 3 hoặc PyTorch/XLA**, nhưng không phù hợp nếu code PyTorch của bạn dùng nhiều CUDA custom kernels. |
| **v5e-1 TPU**<br> | **Google Cloud TPU v5e** *(1 chip)* | **16 GB HBM** | ~1.2 – 2.0 CU / giờ | Thế hệ TPU tiền nhiệm (197 TFLOPS BF16), thay thế cho dòng TPU v2-8 cũ trước đây. Phù hợp để thử nghiệm pipeline trên JAX/TensorFlow quy mô nhỏ. |

(Lưu ý thêm về nút **High-RAM**: Nút này đang bị ẩn khi bạn chọn G4/A100/L4 vì các máy ảo đi kèm những GPU cao cấp này vốn đã được Google cấu hình sẵn lượng **System RAM rất lớn (từ 50 GB đến hơn 80 GB RAM hệ thống)** theo mặc định, không cần phải gạt bật thủ công như khi dùng CPU hay T4).

Bạn đang dự định dùng Colab để huấn luyện hay chạy thử nghiệm loại mô hình nào để mình gợi ý cách chọn GPU tiết kiệm điểm CU nhất?