from sqlalchemy.dialects.postgresql import UUID
import uuid

from floggy import db


class ContentType(db.Model):
    __tablename__ = 'content_types'

    id = db.Column(UUID(), primary_key=True)
    name = db.Column(db.String(64))
    uri = db.Column(db.String(64))

