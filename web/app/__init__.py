from flask import Flask
from flask_bootstrap import Bootstrap

boostrap = Bootstrap()


def create_app():

    app = Flask(__name__)
    boostrap.init_app(app)

    # Register src_blueprint
    #
    from .src import src as src_blueprint
    app.register_blueprint(src_blueprint)

    return app

