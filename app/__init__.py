from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.core import core  # import blueprint

    app.register_blueprint(core)  # register blueprint

    from app.projects import projects

    app.register_blueprint(projects)

    return app
