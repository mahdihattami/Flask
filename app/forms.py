from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[DataRequired(), Length(min=2, max=120)],
        render_kw={"placeholder": "Your name", "autocomplete": "name"},
    )
    email = EmailField(
        "Email",
        validators=[DataRequired(), Email(), Length(max=255)],
        render_kw={"placeholder": "you@example.com", "autocomplete": "email"},
    )
    subject = StringField(
        "Subject",
        validators=[DataRequired(), Length(min=3, max=200)],
        render_kw={"placeholder": "Project inquiry"},
    )
    message = TextAreaField(
        "Message",
        validators=[DataRequired(), Length(min=10, max=5000)],
        render_kw={"placeholder": "Tell me about your project…", "rows": 5},
    )
