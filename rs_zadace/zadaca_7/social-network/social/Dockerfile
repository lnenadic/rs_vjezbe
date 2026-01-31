FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY socialAPI.py .

EXPOSE 3500

CMD ["uvicorn", "socialAPI:app", "--host", "0.0.0.0", "--port", "3500"]