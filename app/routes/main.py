from flask import Blueprint, abort, flash, redirect, render_template, request, url_for

from app.forms import ContactForm
from app.services.contact import notify_contact, save_contact_message
from config import EXPERIENCE, FAQ, PROJECTS, SITE, SKILLS, TESTIMONIALS, get_project

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template(
        "index.html",
        projects=PROJECTS[:4],
        skills=SKILLS,
        experience=EXPERIENCE,
        testimonials=TESTIMONIALS,
        stats={
            "years": SITE["years_experience"],
            "projects": SITE["projects_shipped"],
            "clients": SITE["happy_clients"],
        },
    )


@main_bp.route("/about")
def about():
    return render_template(
        "about.html",
        experience=EXPERIENCE,
        skills=SKILLS,
        faq=FAQ,
    )


@main_bp.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@main_bp.route("/projects/<slug>")
def project_detail(slug):
    project = get_project(slug)
    if not project:
        abort(404)
    others = [p for p in PROJECTS if p["slug"] != slug][:3]
    return render_template("project_detail.html", project=project, others=others)


@main_bp.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        save_contact_message(
            form.name.data.strip(),
            form.email.data.strip().lower(),
            form.subject.data.strip(),
            form.message.data.strip(),
        )
        notify_contact(
            form.name.data.strip(),
            form.email.data.strip(),
            form.subject.data.strip(),
            form.message.data.strip(),
        )
        flash("Thanks — your message was sent. I'll reply soon.", "success")
        return redirect(url_for("main.contact"))
    return render_template("contact.html", form=form)


@main_bp.route("/api/health")
def health():
    return {"status": "ok", "service": "portfolio"}


@main_bp.route("/robots.txt")
def robots():
    return render_template("robots.txt"), 200, {"Content-Type": "text/plain; charset=utf-8"}


@main_bp.route("/sitemap.xml")
def sitemap():
    pages = [
        url_for("main.index", _external=True),
        url_for("main.about", _external=True),
        url_for("main.projects", _external=True),
        url_for("main.contact", _external=True),
    ]
    for project in PROJECTS:
        pages.append(url_for("main.project_detail", slug=project["slug"], _external=True))
    return (
        render_template("sitemap.xml", pages=pages),
        200,
        {"Content-Type": "application/xml; charset=utf-8"},
    )
