import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-in-production")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{BASE_DIR / 'instance' / 'portfolio.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL", "hello@example.com")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "true").lower() == "true"
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False


SITE = {
    "name": "Mahdi Siwa",
    "tagline": "Software crafted with clarity.",
    "role": "Full-Stack Developer",
    "location": "Available worldwide",
    "email": "hello@example.com",
    "github": "https://github.com",
    "linkedin": "https://linkedin.com",
    "twitter": "https://twitter.com",
    "resume_url": "/static/files/resume.pdf",
    "years_experience": 5,
    "projects_shipped": 24,
    "happy_clients": 18,
}

TESTIMONIALS = [
    {
        "quote": "Mahdi delivered a polished product on time — the UX feels effortless.",
        "author": "Alex Chen",
        "role": "Product Lead",
    },
    {
        "quote": "Clear communication, solid architecture, and attention to detail throughout.",
        "author": "Sarah Miller",
        "role": "Startup Founder",
    },
    {
        "quote": "Our API latency dropped significantly after the refactor. Highly recommend.",
        "author": "James Okonkwo",
        "role": "Engineering Manager",
    },
]

PROJECTS = [
    {
        "slug": "nebula",
        "title": "Nebula",
        "subtitle": "Cloud analytics, reimagined.",
        "description": "Real-time dashboards with sub-second queries and a calm, focused interface.",
        "long_description": (
            "Nebula aggregates telemetry from distributed services into a single pane of glass. "
            "Built with streaming pipelines and a React front end tuned for large datasets."
        ),
        "tags": ["Python", "React", "PostgreSQL"],
        "theme": "dark",
        "accent": "#6366f1",
        "year": "2025",
        "url": "#",
        "highlights": ["Sub-second queries", "Role-based access", "Export to PDF"],
    },
    {
        "slug": "pulse",
        "title": "Pulse",
        "subtitle": "Health tracking. Simplified.",
        "description": "A mobile-first wellness app with gentle insights and privacy by design.",
        "long_description": (
            "Pulse helps users track habits without guilt. End-to-end encryption for health data "
            "and a Flask API powering sync across devices."
        ),
        "tags": ["Flask", "Swift", "Redis"],
        "theme": "light",
        "accent": "#ec4899",
        "year": "2024",
        "url": "#",
        "highlights": ["Offline-first mobile", "HIPAA-minded design", "Weekly insights"],
    },
    {
        "slug": "atlas",
        "title": "Atlas",
        "subtitle": "Maps for teams.",
        "description": "Collaborative geospatial tooling for logistics and field operations.",
        "long_description": (
            "Atlas layers team annotations on Mapbox with live location sharing and route optimization "
            "for field crews."
        ),
        "tags": ["TypeScript", "Mapbox", "Node"],
        "theme": "gradient",
        "accent": "#0ea5e9",
        "year": "2024",
        "url": "#",
        "highlights": ["Live collaboration", "Custom map styles", "Webhook integrations"],
    },
    {
        "slug": "forge",
        "title": "Forge",
        "subtitle": "Build. Ship. Repeat.",
        "description": "Developer platform with CI pipelines and one-click deploys.",
        "long_description": (
            "Forge unifies git hosting, build pipelines, and preview environments for small teams "
            "who want Heroku-like simplicity on their own infra."
        ),
        "tags": ["Go", "Docker", "Kubernetes"],
        "theme": "dark",
        "accent": "#f97316",
        "year": "2023",
        "url": "#",
        "highlights": ["Preview URLs per PR", "Built-in secrets", "Usage dashboards"],
    },
]

SKILLS = [
    {"name": "Backend", "items": ["Python", "Flask", "Django", "REST & GraphQL"]},
    {"name": "Frontend", "items": ["HTML/CSS", "JavaScript", "React", "Responsive UI"]},
    {"name": "Data", "items": ["PostgreSQL", "SQLite", "Redis", "SQLAlchemy"]},
    {"name": "Tools", "items": ["Git", "Docker", "Linux", "CI/CD"]},
]

EXPERIENCE = [
    {
        "period": "2023 — Present",
        "title": "Software Engineer",
        "place": "Independent & contract work",
        "detail": "End-to-end web products, APIs, and polished user experiences.",
    },
    {
        "period": "2021 — 2023",
        "title": "Developer",
        "place": "Startups & teams",
        "detail": "Shipped features from prototype to production with measurable impact.",
    },
]

FAQ = [
    {
        "question": "What types of projects do you take on?",
        "answer": "Web apps, APIs, MVPs, and redesigns — especially where UX and performance matter.",
    },
    {
        "question": "Do you work remotely?",
        "answer": "Yes. I'm based for UTC+4:30 and collaborate async-friendly across time zones.",
    },
    {
        "question": "What's your typical timeline?",
        "answer": "MVPs often land in 4–8 weeks; larger builds are scoped in phases with clear milestones.",
    },
]


def get_project(slug: str):
    for project in PROJECTS:
        if project["slug"] == slug:
            return project
    return None
