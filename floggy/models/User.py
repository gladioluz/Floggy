from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime

from floggy import db, login, jwt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(), primary_key=True)
    avatar = db.Column(db.String(256))
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(16))

    registered = db.Column(db.DateTime)
    active = db.Column(db.Boolean)

    is_anonymous = False

    def __init__(self, avatar, username, email, role):
        self.id = uuid.uuid4().urn
        self.avatar = avatar
        self.username = username
        self.email = email
        self.role = role
        self.datetime = datetime.datetime.utcnow()
        self.active = True

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def get_id(self):
        return self.id

    def get_urole(self):
        return self.role

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@jwt.user_loader_callback_loader
def jwt_load_user(identity):
    return User.query.get(identity['id'])
