from flask import Flask

from .config import Config
from .src.utils import DOCUMENTS


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.config['UPLOAD_FOLDER'] = DOCUMENTS

    from .views import views
    app.register_blueprint(views)

    return app
