from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_recaptcha import ReCaptcha
from logging.handlers import RotatingFileHandler
import logging

from config import Config, LOG_FILE
from floggy.core.converters import UUIDConverter

db = SQLAlchemy()
jwt = JWTManager()
login = LoginManager()
recaptcha = ReCaptcha()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login.init_app(app)
    jwt.init_app(app)

    app.url_map.converters['uuid'] = UUIDConverter

    file_handler_error = RotatingFileHandler(
        LOG_FILE, maxBytes=1024 * 1024 * 100, backupCount=20
    )
    file_handler_error.setLevel(logging.ERROR)
    app.logger.addHandler(file_handler_error)

    return app
