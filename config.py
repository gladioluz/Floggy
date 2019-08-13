import os
import datetime
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

APP_FOLDER = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FOLDER = APP_FOLDER + "/app/templates"

EXTERNAL_DIR = os.path.dirname(APP_FOLDER)

LOG_PATH = EXTERNAL_DIR + '/logs'
LOG_FILE = LOG_PATH + '/errors_log.log'
MEDIA_PATH = EXTERNAL_DIR + '/media'

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

if not os.path.exists(MEDIA_PATH):
    os.makedirs(MEDIA_PATH)


class Config(object):
    SERVER_NAME = os.getenv('SERVER_NAME')
    SECRET_KEY = os.getenv('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        os.getenv('POSTGRES_USER'),
        os.getenv('POSTGRES_USER_PASSWORD'),
        os.getenv('POSTGRES_HOST'),
        os.getenv('POSTGRES_PORT'),
        os.getenv('POSTGRES_NAME')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=24)

    DEBUG = False
    TESTING = False
