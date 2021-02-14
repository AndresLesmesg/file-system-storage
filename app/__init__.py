from flask import Flask

from .config import Config
from .src.utils import STORAGE_DIR


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.config['UPLOAD_FOLDER'] = STORAGE_DIR

    from .views import views
    app.register_blueprint(views)

    return app
