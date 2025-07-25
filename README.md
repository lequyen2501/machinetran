# Machine Translation with LSTM (Seq2Seq)

## LSTM trong Dịch Máy là gì?

Dự án sử dụng kiến trúc **Encoder–Decoder với LSTM**, một dạng mạng học sâu phổ biến trong xử lý ngôn ngữ tự nhiên, để dịch từ tiếng Đức sang tiếng Anh. Đây là một kỹ thuật học sâu thường dùng trong các hệ thống dịch máy tuần tự (sequence-to-sequence learning).

---

## Mô tả dự án

Dự án bao gồm hai phần:

1. **Huấn luyện mô hình dịch máy** từ tiếng Đức sang tiếng Anh (German → English) sử dụng TensorFlow và LSTM.
2. **Triển khai Flask App** giao diện web cho phép người dùng dịch câu nhập vào.

---

## 1. Huấn luyện mô hình (Model Training)

### File huấn luyện:

* `machine-translation-final.ipynb`

### Dữ liệu:

* `deu.txt`: file text chứa câu dịch tiếng Đức - tiếng Anh (ngăn cách bằng tab)
* Tải về tại: [https://www.kaggle.com/datasets/alincijov/bilingual-sentence-pairs]

### Pipeline huấn luyện:

* Tiền xử lý: loại bỏ dấu câu, viết thường, token hoá, padding
* Mô hình: Encoder-Decoder với LSTM
* Epochs: 30 | Batch size: 512
* Loss: `sparse_categorical_crossentropy` | Optimizer: `RMSprop`

### Output sau khi huấn luyện:

* `model.keras`: mô hình đã huấn luyện
* `tokenizer_de.pkl`: tokenizer tiếng Đức (input)
* `tokenizer_en.pkl`: tokenizer tiếng Anh (output)

---

## 2. Flask Web App

### File:

* `app.py`: Flask backend
* `templates/index.html`: giao diện người dùng

### Cách chạy app:

```bash
pip install -r requirements.txt
python app.py
```

Sau đó mở trình duyệt:

```
http://127.0.0.1:5000
```

### Backend logic:

* Load model + tokenizer
* Tiến hành token hoá câu input, pad, dự đoán output
* Trả về câu dịch


## Tổng kết

* Dự án giúp hiểu quy trình NLP, dịch máy với kiến trúc Encoder-Decoder sử dụng LSTM.
* Dễ triển khai web dưới dạng demo nhỏ gọn với Flask.

---
Tác giả

Dự án NLP demo bởi Nguyễn Thị Lệ Quyền