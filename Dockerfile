FROM python:3.9-slim

WORKDIR /app

COPY app.py /app/
COPY templates /app/templates

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
