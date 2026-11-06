# Rules for Claude in this repo

Đọc [SOUL.md](SOUL.md) trước khi bắt đầu: nó ghi người dùng là ai, muốn gì, làm việc thế nào.

## 1. Research trước, giải pháp sau
- Trước khi đề xuất giải pháp, thiết kế thí nghiệm, chọn model/thư viện hay viết phần related work, tìm và đọc nguồn trước: paper, docs chính thức, repo, dataset card. Không trả lời từ trí nhớ cho những thứ có thể đã thay đổi (API, giá, model, phiên bản thư viện, paper mới).
- Ưu tiên nguồn gốc: paper peer-reviewed, arXiv, docs chính thức, GitHub của tác giả. Ghi rõ giấy phép khi dùng dữ liệu hoặc code.
- Mỗi đợt research có từ 2 nguồn trở lên được lưu thành một file trong `research/YYYY-MM-DD-<chủ-đề>.md`, theo [research/_template.md](research/_template.md): câu hỏi, truy vấn đã chạy, nguồn (link, đã đọc gì, rút ra gì), kết luận, điều còn chưa chắc.
- Trong câu trả lời, dẫn link tới nguồn. Nếu không tìm được nguồn thì nói rõ là đang suy luận.

## 2. Journal
- Ghi mọi buổi làm việc vào [JOURNAL.md](JOURNAL.md): mục mới nhất ở trên cùng, tiêu đề `## YYYY-MM-DD — <việc chính>`.
- Mỗi mục gồm: **Vấn đề**, **Đã làm / giải pháp**, **Kết quả** (số liệu, lỗi, file đã đổi, commit), **Hình/chart** (link tới `images/` hoặc file kết quả), **Còn lại / bước tiếp**, link tới file research nếu có.
- Cập nhật journal trước khi kết thúc lượt làm việc có thay đổi file hoặc kết quả chạy. Ảnh, chart, video lưu trong `images/<YYYY-MM-DD>-<tên>.png` (hoặc thư mục `results/` của thí nghiệm) và nhúng vào journal bằng link tương đối.

## 3. Môi trường ảo khi chạy trên máy
- Không bao giờ `pip install` vào Python hệ thống hoặc conda `base`.
- Mặc định dùng **uv**: `uv venv .venv && source .venv/bin/activate && uv pip install -r requirements.txt` (hoặc `uv run ...`). Mỗi thí nghiệm có `.venv/` và `requirements.txt` riêng trong thư mục của nó.
- Chỉ dùng **conda** khi cần gói không phải Python (CUDA, gói hệ thống): `conda create -n <tên-thí-nghiệm> python=3.11`.
- Ghi lại các dependency mới vào `requirements.txt`. `.venv/` không được commit.
- Notebook chạy trên Colab không cần venv. Khi chạy thử phần logic của chúng ở máy local thì vẫn dùng venv.

## 4. Cá nhân hóa
- Khi rút ra được điều mới về ý định, sở thích hay thói quen của người dùng (từ lời họ nói, cách họ sửa, cái họ chọn), cập nhật [SOUL.md](SOUL.md). Ghi kèm bằng chứng và ngày. Sửa hoặc xóa những điều đã sai, không chỉ thêm vào.

## Quy ước có sẵn
- Trả lời bằng tiếng Việt. Code, comment và paper viết bằng tiếng Anh.
- Không ghi API key hay token vào bất kỳ file nào. Chỉ dùng Colab Secrets hoặc biến môi trường.
- Không dùng dữ liệu do LLM tự sinh làm dữ liệu nghiên cứu. Dùng bộ công khai, ghi nguồn và giấy phép. Mọi phần dịch hay chuyển thể phải được người dùng duyệt trước khi dùng.
- Chỉ commit hoặc push khi người dùng yêu cầu.
