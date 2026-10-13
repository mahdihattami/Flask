from flask import Flask, Blueprint
from .routes import main
from .extensions import db
def create_app():
    app = Flask(__name__)
    main = Blueprint("main",__name__)
    @main.route("/")
    def index():
        return "<h1>Using Blueprint</h1>"



    app.register_blueprint(main)

    return app