FROM python:3.13-slim

WORKDIR /app

COPY src/ ./src/
COPY requirements.txt .
COPY service_account.json .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/app/src/colab_bg.py"]