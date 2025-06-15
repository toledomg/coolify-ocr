FROM python:3.10-slim

WORKDIR /app

RUN apt update && \
    apt install -y tesseract-ocr tesseract-ocr-por libglib2.0-0 libsm6 libxext6 libxrender-dev && \
    pip install flask pillow pytesseract

COPY ocr-api.py /app/ocr-api.py

EXPOSE 9000

CMD ["python", "/app/ocr-api.py"]
