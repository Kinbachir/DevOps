FROM python:3.9-slim

WORKDIR /app

COPY app.py app.py

RUN apt-get update && apt-get install -y --no-install-recommends python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["python", "app.py"]
