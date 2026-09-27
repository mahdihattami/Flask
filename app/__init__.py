import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask

from app.extensions import csrf, db
from config import Config


def create_app(config_class=Config):
    load_dotenv()
    flask_app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder="../templates",
        static_folder="../static",
    )
    flask_app.config.from_object(config_class)

    instance_path = Path(flask_app.instance_path)
    instance_path.mkdir(parents=True, exist_ok=True)

    db.init_app(flask_app)
    csrf.init_app(flask_app)

    import app.models  # noqa: F401

    with flask_app.app_context():
        db.create_all()

    from app.routes.errors import errors_bp
    from app.routes.main import main_bp

    flask_app.register_blueprint(main_bp)
    flask_app.register_blueprint(errors_bp)

    register_cli(flask_app)

    @flask_app.context_processor
    def inject_globals():
        from config import SITE

        return {"site": SITE, "current_year": 2026}

    return flask_app


def register_cli(flask_app):
    import click

    from app.models import ContactMessage

    @flask_app.cli.command("list-messages")
    @click.option("--limit", default=20, help="Number of messages to show.")
    def list_messages(limit):
        """Print recent contact form submissions."""
        rows = (
            ContactMessage.query.order_by(ContactMessage.created_at.desc())
            .limit(limit)
            .all()
        )
        if not rows:
            click.echo("No messages yet.")
            return
        for row in rows:
            click.echo(f"{row.created_at.isoformat()} | {row.email} | {row.subject}")
