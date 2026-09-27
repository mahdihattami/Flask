# Flask Portfolio

Apple-inspired personal portfolio built with Flask — multi-page site, project case studies, contact form with SQLite storage, and deployment-ready structure.

## Features

- Home, About, Projects, Project detail, and Contact pages
- Frosted navigation, scroll animations, stats counters, testimonials
- Contact form (CSRF-protected) saves messages to SQLite; optional SMTP in `.env`
- SEO: Open Graph meta, JSON-LD, `robots.txt`, `sitemap.xml`
- Custom 404 / 500 pages
- Health check at `/api/health`
- Pytest test suite

## Setup

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Edit `config.py` for your bio, projects, and links. Set `SECRET_KEY` in `.env` before production.

## Run

```powershell
python run.py
```

Open http://127.0.0.1:5000

## Production

Use `wsgi.py` with gunicorn or waitress:

```powershell
pip install gunicorn
gunicorn -w 2 -b 0.0.0.0:8000 wsgi:app
```

## Tests

```powershell
pytest
```

## CLI

List stored contact messages:

```powershell
flask --app run.py list-messages
```

Replace `static/files/resume.pdf` with your own CV.
