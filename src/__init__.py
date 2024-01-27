from flask import flask

# Routes
from .routes import IndexRoutes

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprint
    app.register_blueprint(IndexRoutes.main, url_prefix="/")

    return app
