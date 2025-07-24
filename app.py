from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import pickle

app = Flask(__name__)

# Load mô hình và tokenizer
model = tf.keras.models.load_model("model/model (2).keras")

with open("model/tokenizer_de (2).pkl", "rb") as f:
    tokenizer_de = pickle.load(f)
with open("model/tokenizer_en (2).pkl", "rb") as f:
    tokenizer_en = pickle.load(f)

max_len_input = 20  # Độ dài câu tối đa (tuỳ chỉnh theo mô hình)

# Hàm dịch câu
def translate_sentence(sentence):
    sequence = tokenizer_de.texts_to_sequences([sentence])  # Chuyển câu thành dãy số
    padded = tf.keras.preprocessing.sequence.pad_sequences(sequence, maxlen=max_len_input, padding='post')  # Padding nếu cần
    
    prediction = model.predict(padded)  # Dự đoán dịch
    predicted_seq = np.argmax(prediction[0], axis=1)  # Chọn giá trị có xác suất cao nhất cho mỗi từ
    output_words = tokenizer_en.sequences_to_texts([predicted_seq])  # Chuyển dãy số thành từ
    return output_words[0].strip()  # Trả về kết quả dịch
# Trang chủ (hiển thị giao diện)
@app.route("/")
def index():
    return render_template("index.html")

# API dịch văn bản
@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()  # Lấy dữ liệu từ frontend
    input_text = data["text"]
    translated = translate_sentence(input_text)  # Dịch câu
    return jsonify({ "translation": translated })  # Trả kết quả dịch về cho frontend

if __name__ == "__main__":
    app.run(debug=True)
