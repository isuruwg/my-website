import os
from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
def create_app(config_type): # dev, test or prod
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')

    app.config.from_pyfile(configuration)

    bootstrap.init_app(app) # initialize bootstrap
    
    from app.core import core    # import blueprint
    app.register_blueprint(core)    # register blueprint

    return app

