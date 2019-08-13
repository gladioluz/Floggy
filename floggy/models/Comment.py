from sqlalchemy.dialects.postgresql import UUID
import uuid
import time

from floggy import db


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(UUID(), primary_key=True)
    user_id = db.Column(UUID(), db.ForeignKey('users.id'), index=True)
    content_id = db.Column(UUID(), db.ForeignKey('contents.id'), index=True)
    body = db.Column(db.Text())

    created = db.Column(db.DateTime)
