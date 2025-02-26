from flask import Flask, render_template, request, send_file, jsonify
import os
import cv2
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = "uploads/"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def encode_message(image_path, message, secret_key):
    img = cv2.imread(image_path)
    full_message = secret_key + "###" + message + "#####"
    binary_msg = ''.join(format(ord(char), '08b') for char in full_message)
    
    idx = 0
    rows, cols, channels = img.shape
    total_pixels = rows * cols * 3

    if len(binary_msg) > total_pixels:
        return None  

    for i in range(rows):
        for j in range(cols):
            for k in range(3):
                if idx < len(binary_msg):
                    img[i, j, k] = (img[i, j, k] & ~1) | int(binary_msg[idx])
                    idx += 1
                else:
                    break

    encoded_path = os.path.join(UPLOAD_FOLDER, "encoded_image.png")
    cv2.imwrite(encoded_path, img)
    return encoded_path

def decode_message(image_path, secret_key):
    img = cv2.imread(image_path)
    binary_msg = ""

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                binary_msg += str(img[i, j, k] & 1)

    decoded_chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    extracted_message = "".join(chr(int(char, 2)) for char in decoded_chars)
    
    if "###" in extracted_message:
        extracted_key, extracted_msg = extracted_message.split("###", 1)
        extracted_msg = extracted_msg.split("#####")[0]

        if extracted_key == secret_key:
            return extracted_msg  
        else:
            return "Invalid Secret Key!"
    return "No Hidden Message Found"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encode", methods=["POST"])
def encode():
    file = request.files["image"]
    message = request.form["message"]
    secret_key = request.form["secret_key"]
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)
    
    encoded_path = encode_message(file_path, message, secret_key)
    
    if encoded_path:
        return send_file(encoded_path, as_attachment=True)
    else:
        return "Error: Message too long for this image.", 400

@app.route("/decode", methods=["POST"])
def decode():
    file = request.files["image"]
    secret_key = request.form["secret_key"]
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)
    
    hidden_message = decode_message(file_path, secret_key)
    return jsonify({"message": hidden_message})

if __name__ == "__main__":
    app.run(debug=True)
