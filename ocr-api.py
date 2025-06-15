from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import os

app = Flask(__name__)


@app.route("/ocr", methods=["POST"])
def ocr():
    if "file" not in request.files:
        return jsonify({"error": "No file"}), 400
    img_file = request.files["file"]
    path = "/tmp/image.png"
    img_file.save(path)
    try:
        text = pytesseract.image_to_string(
            Image.open(path), lang="por"
        )  # Use "eng" para inglês, "por" para português
    except Exception as e:
        os.remove(path)
        return jsonify({"error": str(e)}), 500
    os.remove(path)
    return jsonify({"text": text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
