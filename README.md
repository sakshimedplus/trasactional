# Transactional Webhook (Django + Celery + Redis)

A production-ready Django application designed to process and manage webhooks asynchronously using **Celery** and **Redis**.
This project is containerized with **Docker** and deploys seamlessly on **Render.com**.

---

## 🚀 Features

* Django-based backend (Python 3.11)
* Asynchronous task queue using **Celery**
* **Redis** as broker and result backend
* **Gunicorn** for production WSGI server
* Fully containerized setup with **Docker**
* Cloud-ready deployment (Render, Azure, etc.)

---

## 🧱 Project Structure

```
.
├── transatioional_webhook/      # Django project directory
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
│   └── wsgi.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚙️ Environment Variables

Before running the project, ensure these variables are set in your Render **Environment** tab or `.env` file locally:

| Variable               | Description                                                                                                                      |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `DJANGO_SECRET_KEY`    | Django secret key (`python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`) |
| `DATABASE_URL`         | Your PostgreSQL database connection string                                                                                       |
| `REDIS_URL`            | Redis Cloud or local Redis URL (e.g., `redis://default:<password>@<host>:<port>`)                                                |
| `DJANGO_DEBUG`         | `True` for local, `False` for production                                                                                         |
| `DJANGO_ALLOWED_HOSTS` | Your Render domain (e.g., `transactional-webhook.onrender.com`)                                                                  |

---

## 🐳 Local Development (Docker)

### 1. Build and Run Containers

```bash
docker compose up --build
```

### 2. Run Migrations

```bash
docker exec -it <container_name> python manage.py migrate
```

### 3. Create Superuser

```bash
docker exec -it <container_name> python manage.py createsuperuser
```

### 4. Access the App

Visit:
👉 [http://localhost:8000](http://localhost:8000)

Admin panel:
👉 [http://localhost:8000/admin](http://localhost:8000/admin)

---

## ☁️ Deployment (Render.com)

1. Push this repository to GitHub.
2. Create a new **Web Service** on Render.
3. Choose **“Deploy from a Dockerfile”**.
4. Add all environment variables (see above).
5. Deploy 🚀

Render automatically rebuilds on every Git push.

---

## ⚡ Celery & Redis

The app uses Celery workers for async background jobs.

To run Celery manually (if not using docker-compose):

```bash
celery -A transatioional_webhook worker --loglevel=info
```

---


---

## 🛠 Tech Stack

* **Backend:** Django 5+
* **Queue:** Celery + Redis
* **Database:** PostgreSQL
* **Server:** Gunicorn
* **Containerization:** Docker
* **Cloud Platform:** Render.com

---

## 👩‍💻 Author

**Sakshi Dubey**
Full Stack Developer — Python | Django | React | Angular
9597248829

