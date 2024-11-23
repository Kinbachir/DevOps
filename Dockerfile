FROM python:3.9-slim

WORKDIR /app

# Copy application code into the container
COPY app.py /app/
COPY templates /app/templates

# Install Python dependencies
RUN pip install flask gunicorn

# Expose the port the app will run on
EXPOSE 80

# Use Gunicorn to run the app in production
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0", "app:app"]
