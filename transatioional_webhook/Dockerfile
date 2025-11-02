# Use lightweight Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r ./transactional_webhook/requirements.txt && pip install gunicorn

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start server with Gunicorn
CMD ["gunicorn", "transatioional_webhook.wsgi:application", "--bind", "0.0.0.0:8000"]
