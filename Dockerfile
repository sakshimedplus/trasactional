FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install gunicorn

# Copy project files
COPY . .

# Collect static files (inside your Django project folder)
RUN python transatioional_webhook/manage.py collectstatic --noinput || echo "No static files"

# Expose port
EXPOSE 8000

# Start app with gunicorn
CMD gunicorn transatioional_webhook.wsgi:application --bind 0.0.0.0:8000
