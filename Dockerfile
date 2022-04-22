FROM python:3-alpine

WORKDIR /app
COPY app.py .
COPY templates ./templates
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]