FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

RUN chmod +x wait-for-db.sh

CMD ["./wait-for-db.sh", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
