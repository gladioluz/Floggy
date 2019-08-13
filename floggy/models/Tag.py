from sqlalchemy.dialects.postgresql import UUID
import uuid

from floggy import db


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(UUID(), primary_key=True)
    name = db.Column(db.String(64))
