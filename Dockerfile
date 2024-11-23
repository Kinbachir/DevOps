FROM python:3.9-slim

WORKDIR /app

# Copy application code into the container
COPY app.py /app/
COPY templates /app/templates

# Install Python dependencies
RUN pip install flask flask-bcrypt flask-sqlalchemy werkzeug

# Expose the port the app will run on
EXPOSE 80

# Use flask to run the app in production
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
