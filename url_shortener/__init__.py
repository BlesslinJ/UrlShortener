from flask import Flask
from .database import db
from .config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from .routes import main
    app.register_blueprint(main)

    return app