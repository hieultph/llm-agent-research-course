# Review 1: kế hoạch cải thiện

> [!summary] Tóm tắt (VI)
> Reviewer khen phần đo lường (§IV) và phần so sánh lời nhắc với khôi phục dấu (§VII-A/B). Bốn vấn đề lớn:
> 1. Biến ambiguity không thể ước lượng được khi có fixed effect item×condition.
> 2. Kết quả "surprise" bị diễn giải như quan hệ nhân quả.
> 3. So sánh mô hình thích nghi tiếng Việt dùng sai mô hình gốc để đối chứng.
> 4. p-value quá nhỏ khi chỉ có 19 cluster.
>
> Sau khi đọc lại code v4–v6: reviewer đúng ở cả 4 điểm, và còn bắt được một lỗi đếm của bài (có 4 mô hình thích nghi, không phải 3).
>
> Kế hoạch có 5 giai đoạn:
> - **A:** chỉ sửa chữ.
> - **B:** phân tích lại trên CPU, dùng dữ liệu sẵn có, không tốn CU.
> - **C:** bạn tự thêm dấu tay cho khoảng 100 bình luận.
> - **D:** chạy GPU v7. Ước tính khoảng 20–30 CU trên L4 và khoảng 25 CU trên A100.
> - **E (tùy chọn):** thêm Gemma và một mô hình 32B, khoảng 30–40 CU.
>
> Nên làm A và B trước vì không tốn CU, và vì kết quả của B quyết định D cần chạy những gì.

## Trạng thái (30/10/2026)

- **Giai đoạn A — xong.** Các phần đã sửa trong `latex/main.tex`:
  - §VI đổi tên thành "What Predicts Errors?"; Bảng V tách thành các panel A/A′/B/C, mỗi panel là một hồi quy riêng;
  - §V dùng 4 mô hình thích nghi, có ghi chú về mô hình gốc, và thêm Bảng V (suy luận với ít cluster);
  - §III-D ghi `enable_thinking=False`, vị trí của prefill và cách chuẩn hóa NLL;
  - abstract, §IV-D, §VIII và Limitations;
  - Hình 1–2 vẽ lại bằng pgfplots từ dữ liệu cuối cùng.
- **Giai đoạn B — xong** (notebook `1A_pilot_v7_cpu.ipynb`, Colab CPU, 9/9 kiểm tra đạt):
  - **B1:** wild bootstrap p = 0,001 cho xu hướng kích thước; p = 0,16 cho so sánh mô hình thích nghi.
  - **B2:** prior lấy từ input có nhiễu chỉ lấy lại 7%.
  - **B3:** comment tự nhiên chỉ đạt mức của văn bản bị bỏ dấu (0,45 so với clean 0,56).
  - **B4:** 14/15 cặp 14B sau khi khôi phục vẫn dưới clean.
  - **B6:** bỏ Phi và Mistral thì Δbroken còn mạnh hơn (−6,3).
- **B5 (rò rỉ dữ liệu test vào bộ khôi phục):** không cần tính. Model card và blog cho biết bộ khôi phục được huấn luyện trên tiêu đề báo (corpus Binhvq), không trùng miền với các tập test. Đã ghi vào bài.
- **Phát hiện lỗi:** tập natural ban đầu có **270** comment, không phải 313 (bỏ 44, còn 226). Đã sửa trong README và trong bài.
- **Giai đoạn C — file đã sẵn sàng:** `MyDrive/llm-research/1A-pilot-v7-cpu/data/natural_sample_100.csv`. Pool chỉ có 17 comment offensive, nên mẫu gồm 53 clean, 17 offensive và 30 hate.
- **Thêm vào D4:** chấm điểm các mô hình trên 100 comment đã được thêm dấu tay. Đây là cách tách hai giải thích còn lại: bộ khôi phục kém trên văn phong mạng xã hội, hay bản thân comment khó.

## Đã kiểm tra trong code (trả lời được ngay)

| Câu hỏi | Câu trả lời | Nguồn |
|---|---|---|
| Q1: ambiguity được ước lượng thế nào? | Từ **một hồi quy khác**: LPM `flip ~ amb + ΔNLL + Δtok + C(model) + C(task) + C(cond)`, chỉ trên các điều kiện partial/strip, cluster theo item. Hồi quy này **không** có fixed effect item×condition. Ambiguity không thay đổi theo mô hình, nên nó không thể đưa vào mô hình chính. Bảng V gộp hai hồi quy này mà không ghi chú, và reviewer đúng | `build_v4.py:1375-1386` |
| Q2: NLL được chuẩn hóa thế nào? | ΔNLL = (tổng NLL trên các token của trường input khi có nhiễu − tổng NLL khi sạch) / **số âm tiết của câu sạch**. Mẫu số không phụ thuộc tokenizer. Tổng NLL của cả chuỗi về lý thuyết không đổi khi số token đổi, nên việc Phi và Mistral được ít token hơn không làm lệch ΔNLL một cách cơ học. Có thể thêm bản chuẩn hóa theo byte để kiểm tra độ bền | `build_v4.py:1283-1291` |
| Q5: Qwen3 có bật chế độ thinking không? | **Không**: `enable_thinking=False` khi dựng template. Phần prefill "Đáp án:" được nối vào sau lượt assistant của template. Cần ghi rõ điều này trong §III-D và kiểm tra lại cùng với khối `<think></think>` rỗng mà template của Qwen3 tự chèn | `build_v4.py:531-535` |
| Q7: hiệu chỉnh bằng prior lấy từ chính các input có nhiễu? | **v4 đã tính** (`pred_percond`: prior lấy trên các item test của từng điều kiện, không dùng nhãn), nhưng bài chưa báo cáo. Chỉ cần lấy số từ `tables/table_robustness` trên Drive | `build_v4.py:1144-1145` |
| Số mô hình thích nghi | `MODEL_INFO` đánh dấu **4** mô hình (SeaLLMs-v3 1.5B/7B, VinaLLaMA 2.7B/7B), và F2 đã dùng cả 4. Chữ "three" trong §V là lỗi khi viết | `build_v4.py:102-117` |
| Mẫu natural bị chọn lọc theo hành vi của bộ khôi phục (điểm 6) | Đúng: 87 trong 313 comment bị loại **trước khi chấm điểm**, nên chưa có dự đoán cho chúng. Cần một lượt GPU nhỏ (giai đoạn D) | `build_v6.py:159-161` |

Những điều reviewer khẳng định cần kiểm chứng trên model card trước khi viết vào bài: SeaLLMs-v3 dựa trên Qwen2, VinaLLaMA-7B dựa trên Llama-2, và phi-4 khác Phi-3.5 về dữ liệu huấn luyện.

## Bảng theo dõi từng ý của reviewer

| # | Ý | Đồng ý? | Hành động | Giai đoạn |
|---|---|---|---|---|
| M1 | Ambiguity bị hấp thụ bởi fixed effect | Đúng | Tách Bảng V: (a) mô hình cùng item, (b) tập con dùng chung tokenizer, (c) mô hình ambiguity với FE model+task+cond. Ghi chú hồi quy nguồn cho từng dòng | A |
| M2 | Diễn giải "surprise" như nhân quả | Đúng | Đổi tiêu đề §VI thành "What predicts errors". Viết "ΔNLL predicts errors", bỏ "Why". Ở §VIII, chuyển ý về huấn luyện thành giả thuyết cần kiểm chứng | A |
| M3 | So sánh mô hình thích nghi bị nhiễu | Đúng | Thêm đối chứng đúng gốc: Qwen2-1.5B/7B-Instruct cho SeaLLMs-v3, Llama-2-7b-chat cho VinaLLaMA-7B. Viết lại §V với các cặp này và sửa "three" → "four". Nếu không chạy được cặp nào thì giảm §V xuống thành mô tả | A + D1 |
| M4 | Inference khi có ít cluster | Đúng | Báo cáo p theo t(G−1) và wild cluster bootstrap (Webb weights, 9999 lần) cho xu hướng kích thước và F2. Thêm: hồi quy bỏ 14B, bỏ họ Phi, chỉ dùng các họ có ≥ 3 cỡ. Viết "continues to 14B" thành "holds when three 14B models are added" | B1 + A |
| 5a | LLM tự khôi phục dấu (2 bước) | Đúng, đây là đối thủ tự nhiên nhất | Bước 1: mô hình sinh lại văn bản có dấu. Bước 2: chấm điểm như cũ. Đo cả độ chính xác khôi phục dấu theo từ | D2 |
| 5b | Few-shot với ví dụ không dấu | Đúng | 3-shot, ví dụ không dấu lấy từ dev, cố định theo seed. Chạy cả clean và strip | D3 |
| 5c | Prior lấy từ input có nhiễu | Đã có dữ liệu | Báo cáo `pred_percond`: mức giảm và phần lấy lại được, so với khôi phục dấu. Có liên hệ với 19/74 cặp sụp về một nhãn | B2 |
| 6a | So natural với comment có dấu cùng lớp | Đúng | So balanced accuracy trên 226 (và 313) comment natural với các comment ViHSD sạch cùng lớp, chuẩn hóa theo lớp. Dùng dự đoán đã có của v4/v6 | B3 (+ D4 cho 87 comment chưa chấm) |
| 6b | Độ chính xác của bộ khôi phục trên mẫu thêm dấu tay | Đúng | Bạn thêm dấu tay cho 100 comment, chọn ngẫu nhiên phân tầng theo lớp. Mình chuẩn bị sẵn file CSV gồm bản gốc và bản máy khôi phục để bạn sửa | C |
| 6 | Bộ lọc ≥ 20% | Đúng | Chấm thêm 87 comment bị loại. Báo cáo kết quả có và không có bộ lọc | D4 |
| 7 | Pipeline thực tế: khôi phục mọi input | Đúng | Áp bộ khôi phục cho clean, partial50 và mixed (`clean→restored` …). Báo cáo bộ khôi phục có làm hỏng văn bản đã có dấu không, và mô hình 14B có rơi xuống dưới độ chính xác clean không (v6 đã có số cho strip→restored, cần thêm clean→restored) | B4 (14B, đã có) + D5 |
| 7 | Bộ khôi phục có thể đã thấy tập test | Đúng | Đọc blog và model card để biết dữ liệu huấn luyện. Nếu không rõ thì ghi vào Limitations. Kiểm tra gián tiếp: so độ chính xác khôi phục trên XNLI-vi test với validation và với văn bản ngoài (tin tức sau ngày phát hành mô hình) | B5 |
| 8 | Partial stripping có trọng số theo tần suất | Đúng | Thêm điều kiện `freq10`: bỏ dấu ở khoảng 10% số từ, ưu tiên từ có tần suất cao (khớp liều với teen code). So với `teencode` và `partial` ở cùng liều | D6 |
| Q11 | Δbroken khi bỏ Phi/Mistral/phi-4 | Đúng | Ước lượng lại G2 chỉ trên các tokenizer tách nhiều hơn sau khi bỏ dấu (bỏ cả 3 cùng lúc, không bỏ từng nhóm) | B6 |
| Q12 | Mô hình > 14B hoặc vocab lớn (Gemma) | Nên làm nếu đủ CU | Gemma-3 4B/12B/27B và Qwen2.5-32B-Instruct, chạy trên A100 | E |
| P1 | Hình 1–2 đang là khung chờ, có thể lấy từ lượt chạy cũ | Đúng | Vẽ lại **cả hai hình từ dữ liệu cuối cùng** trong một notebook CPU: liều–đáp ứng trung bình 3 seed, và kích thước gồm cả 14B. Thêm dòng chú thích nguồn dữ liệu | B7 |
| P2 | Abstract lặp "a model" | Đúng | Sửa | A |
| P3 | 0,57 so với 0,52 | Đúng | Ghi rõ tập con ở cả hai chỗ: 74 cặp ≤ 8B so với 85 cặp hợp lệ dưới cả 4 prompt | A |
| P4 | Bảng V gộp nhiều hồi quy | Đúng | Như M1 | A |
| P5 | "half of its task ability" | Đúng | Viết thành "about half of its above-chance accuracy" | A |

## Giai đoạn A: sửa chữ (không cần chạy)

1. §VI: đổi tiêu đề, tách Bảng V (M1, M2, P4), và ghi rõ chuẩn hóa NLL theo âm tiết của câu sạch (Q2).
2. §V: sửa "three" → "four". Ghi chú mô hình gốc của SeaLLMs-v3 và VinaLLaMA. Tạm thời viết phần thích nghi là mô tả cho đến khi có D1 (M3).
3. §III-D: ghi `enable_thinking=False` và vị trí của prefill (Q5).
4. Sửa abstract, §IV-D, §VIII (P2, P3, P5). Bỏ khẳng định nhân quả trong §VIII.
5. Limitations: nguồn dữ liệu huấn luyện của bộ khôi phục, và việc so phi-4 với Phi-3.5 lẫn cả thế hệ mô hình lẫn kích thước.

## Giai đoạn B: phân tích lại trên CPU

Một notebook mới, `1A_pilot_v7_cpu.ipynb`, đọc kết quả v4, v5 và v6 trên Drive. Có smoke test cục bộ như các lần trước.

| | Phân tích | Đầu ra |
|---|---|---|
| B1 | Xu hướng kích thước và F2 với p theo t(G−1) và wild cluster bootstrap. Các hồi quy bỏ 14B, bỏ họ Phi, chỉ dùng họ ≥ 3 cỡ | bảng `size_inference` |
| B2 | Hiệu chỉnh theo từng điều kiện (`pred_percond`): mức giảm, phần lấy lại được, số cặp sụp về một nhãn trước và sau | bảng `noisy_prior` |
| B3 | Natural so với comment có dấu cùng lớp (balanced accuracy theo lớp) | bảng `natural_vs_accented` |
| B4 | Mô hình 14B: độ chính xác sau khôi phục so với clean | bảng `restored_vs_clean` |
| B5 | Độ chính xác của bộ khôi phục trên test và validation (XNLI-vi, VSFC), và trên văn bản ngoài | bảng `restorer_leakage` |
| B6 | Δbroken chỉ trên các tokenizer tách nhiều hơn sau khi bỏ dấu, kèm ΔNLL chuẩn hóa theo byte | bảng `broken_subset` |
| B7 | Vẽ lại Hình 1–2 từ dữ liệu cuối | `fig_dose_final.pdf`, `fig_size_final.pdf` |

## Giai đoạn C: bạn thêm dấu tay

Mình tạo `natural_sample_100.csv` gồm 100 comment chọn ngẫu nhiên phân tầng theo lớp, mỗi dòng có bản gốc không dấu và bản máy khôi phục. Bạn sửa bản máy thành văn bản đúng; ước tính khoảng 1–1,5 giờ. Mình sẽ tính độ chính xác theo từ của bộ khôi phục trên văn bản tự nhiên, so với 75% trên văn bản ViHSD bị bỏ dấu nhân tạo.

## Giai đoạn D: chạy GPU v7

Chạy trên L4 cho 16 mô hình nhỏ cộng 3 mô hình đối chứng, rồi A100 cho 3 mô hình 14B, giống quy trình v6. Mọi điều kiện mới đều qua cổng hợp lệ và có kiểm tra tái lập câu trả lời của v4.

| | Thí nghiệm | Mô hình | Ghi chú |
|---|---|---|---|
| D1 | Đối chứng đúng gốc: clean, strip, restored | Qwen2-1.5B/7B-Instruct, Llama-2-7b-chat (cần `HF_TOKEN`) | Ít tốn |
| D2 | LLM tự khôi phục dấu rồi trả lời | 19 mô hình | Tốn nhất vì phải sinh văn bản. Đề xuất: đủ item cho 4 tác vụ ngắn, ViMMRC giới hạn 120 item |
| D3 | 3-shot với ví dụ không dấu, clean và strip | 19 mô hình | Prompt dài hơn; ViMMRC dùng 1-shot |
| D4 | 87 comment natural bị loại | 19 mô hình | Rất ít tốn |
| D5 | Khôi phục mọi input: clean, partial50, mixed | 19 mô hình | Chỉ cần chấm điểm |
| D6 | `freq10`: bỏ dấu có trọng số theo tần suất | 19 mô hình | Một điều kiện |

Ước tính: L4 khoảng 6–9 giờ (≈ 20–30 CU), A100 cho 14B khoảng 2 giờ (≈ 25 CU). D2 là phần lớn nhất; nếu muốn tiết kiệm, có thể chạy D2 trên 8 mô hình, mỗi họ một mô hình cộng 3 mô hình 14B.

## Giai đoạn E (tùy chọn): kiểm tra xu hướng kích thước có bão hòa không

Gemma-3 4B/12B/27B (vocab 262k, cần `HF_TOKEN`) và Qwen2.5-32B-Instruct trên A100, điều kiện clean, strip và restored. Khoảng 3 giờ A100 (≈ 30–40 CU). Phần này trả lời Q12 và làm khẳng định về kích thước mạnh hơn hẳn. Nếu bỏ qua, ghi vào Limitations.

## Giai đoạn F: sửa bài và viết thư trả lời

- Cập nhật `main.tex`, các bảng và hình, rồi biên dịch lại.
- Viết `response-1.md`: trả lời từng ý (M1–M4, 5–8, P1–P5, Q1–Q12), mỗi ý ghi điểm đã sửa trong bài và số liệu mới.
- Sau đó bạn đọc lại như một vòng review thứ hai.

## Thứ tự đề xuất

A → B → (C, chạy song song với D) → D → (E nếu đủ CU) → F. Giai đoạn A và B không tốn CU và cho biết D2/D3 có thực sự cần không. Ví dụ, nếu `pred_percond` (B2) đã lấy lại được nhiều, cần đưa nó vào bài như một đối thủ chính của khôi phục dấu.
