# Embassy Service App — Backend

A Django-based backend for an embassy services application that enables users to book and monitor appointments, manage documents, receive notifications, and access reports. This repository contains the API, models, and admin configuration used by the frontend or other clients to interact with core embassy services.

---

**Project status:** prototype / early development

**Table of contents**

- **Project**: short description and goals
- **Tech Stack**: frameworks and main dependencies
- **Requirements**: system and Python dependencies
- **Setup**: how to install, configure and run locally
- **Database**: SQLite usage and migrations
- **Apps & Endpoints**: overview of Django apps and responsibilities
- **Testing**: how to run tests
- **Contributing**: guidelines for contributors
- **License & Contact**n

---

**Project**

- **Purpose**: Provide a backend API for booking embassy appointments, uploading/managing documents, sending notifications, and generating reports for users and administrators.
- **Goals**:
  - Allow users to create and monitor appointments.
  - Store and serve documents associated with appointments or user profiles.
  - Deliver notifications about appointment statuses and reminders.
  - Produce simple reports for administrative use.

---

**Tech Stack**

- **Framework**: Django (Python), Django Rest Framework
- **Database**: SQLite (default for local development)
- **Languages**: Python 3.x

---

**Repository Structure (key files)**

- `manage.py`: Django management entrypoint.
- `db.sqlite3`: default local SQLite database (created during development).
- `embassyapp/`: project settings and WSGI/ASGI configuration.
- apps: `appointments/`, `documents/`, `notifications/`, `reports/`, `services/`, `users/` — each contains models, views, admin and migrations.

---

**Requirements**

- Python 3.8+ (recommended 3.10/3.11)
- pip
- Virtual environment tool (venv or similar)

Create a virtual environment and install dependencies (example):

```bash
python -m venv venv
 .\venv\Scripts\Activate
 pip install -U pip
 pip install -r requirements.txt  # if provided
```

If no `requirements.txt` exists in the repo, you can install Django directly for development:

```bash
 pip install Django
```

---

**Setup & Running (development)**

1. Activate your virtual environment (see above).
2. Apply migrations:

```bash
 python manage.py migrate
```

3. Create a superuser (admin) account to access Django admin:

```bash
 python manage.py createsuperuser
```

4. Run the development server:

```bash
 python manage.py runserver
```

Open http://127.0.0.1:8000/ in a browser or access the Django admin at http://127.0.0.1:8000/admin/.

---

**Environment & Configuration**

- The project uses Django settings located in `embassyapp/settings.py`.
- For production, replace SQLite with a production-ready DB (PostgreSQL, MySQL) and configure `ALLOWED_HOSTS`, `SECRET_KEY` and other secure settings via environment variables.
- Example environment variables to set in production:
  - `DJANGO_SECRET_KEY`
  - `DATABASE_URL` (if using dj-database-url)
  - `DEBUG=0` (or `False`)

---

**Database & Migrations**

- This repo uses SQLite for development for simplicity. Migrations are included in each app's `migrations/` folder.
- To create new migrations after model changes:

```bash
 python manage.py makemigrations
 python manage.py migrate
```

---

**Apps Overview**

- `appointments/` — models and endpoints for booking and managing appointment records.
- `documents/` — upload and manage documents associated with users or appointments.
- `notifications/` — logic/models for storing and sending notifications (email/sms hooks can be added).
- `reports/` — generation of simple reports and aggregates for admin use.
- `services/` — domain models for embassy service offerings and related logic.
- `users/` — user profile models and authentication-related views.

---

**Testing**

- Run app tests with Django's test runner:

```
; python manage.py test
```

Add unit tests in each app's `tests.py` (or split into `tests/` modules) to validate models, views and business logic.

---

**Development Tips**

- Use `python manage.py shell` for interactive debugging.
- Use the Django admin to inspect models and data quickly.
- For API work, consider adding Django REST Framework and documenting endpoints with tools like `drf-yasg` or `drf-spectacular`.

---

**Deployment Notes**

- For production deployments, recommended minimal steps:
  - Switch to PostgreSQL or another production-ready DB.
  - Configure static files (collectstatic) and serve them via a CDN or web server.
  - Configure a WSGI server (Gunicorn/uvicorn) behind a reverse proxy (Nginx).
  - Secure secrets and disable `DEBUG`.

---

**Contributing**

- Fork the repository.
- Create a feature branch: `git checkout -b feature/your-feature`.
- Make changes and add tests.
- Submit a pull request describing the changes.

---

**Important Files & Commands**

- Project entry: `manage.py`
- Run dev server: `python manage.py runserver`
- Apply migrations: `python manage.py migrate`
- Create admin user: `python manage.py createsuperuser`


