import logging
import smtplib
from email.message import EmailMessage

from flask import current_app

from app.extensions import db
from app.models import ContactMessage

logger = logging.getLogger(__name__)


def save_contact_message(name: str, email: str, subject: str, message: str) -> ContactMessage:
    record = ContactMessage(name=name, email=email, subject=subject, message=message)
    db.session.add(record)
    db.session.commit()
    return record


def notify_contact(name: str, email: str, subject: str, message: str) -> None:
    """Send email when SMTP is configured; otherwise log only."""
    mail_server = current_app.config.get("MAIL_SERVER")
    to_addr = current_app.config.get("CONTACT_EMAIL")

    body = f"From: {name} <{email}>\n\n{message}"
    if not mail_server:
        logger.info("Contact message saved (SMTP not configured): %s — %s", email, subject)
        return

    msg = EmailMessage()
    msg["Subject"] = f"[Portfolio] {subject}"
    msg["From"] = current_app.config.get("MAIL_USERNAME") or to_addr
    msg["To"] = to_addr
    msg["Reply-To"] = email
    msg.set_content(body)

    try:
        with smtplib.SMTP(mail_server, current_app.config.get("MAIL_PORT", 587)) as smtp:
            if current_app.config.get("MAIL_USE_TLS"):
                smtp.starttls()
            username = current_app.config.get("MAIL_USERNAME")
            password = current_app.config.get("MAIL_PASSWORD")
            if username and password:
                smtp.login(username, password)
            smtp.send_message(msg)
    except OSError as exc:
        logger.warning("Could not send contact email: %s", exc)
