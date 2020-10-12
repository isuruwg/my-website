from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)

    bootstrap.init_app(app)  # initialize bootstrap
    from app.core import core    # import blueprint
    app.register_blueprint(core)    # register blueprint

    return app
