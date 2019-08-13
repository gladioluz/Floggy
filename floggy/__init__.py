import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from logging.handlers import RotatingFileHandler

from config import Config, LOG_FILE
from floggy.utils.converters import UUIDConverter

db = SQLAlchemy()
login = LoginManager()
jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = 'static'
    app.add_url_rule('/static/<path:filename>',
                     endpoint='static',
                     subdomain='admin',
                     view_func=app.send_static_file)

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
