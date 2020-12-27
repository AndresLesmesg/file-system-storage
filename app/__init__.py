from flask import Flask
from .config import Config 

def create_app():
    
    app = Flask(__name__)

    app.config.from_object(Config)

    from .views import views
    app.register_blueprint(views)

    return app