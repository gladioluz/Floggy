from sqlalchemy.dialects.postgresql import UUID
import uuid

from floggy import db


class Rubric(db.Model):
    __tablename__ = 'rubrics'

    id = db.Column(UUID(), primary_key=True)
    name = db.Column(db.String(64))
    uri = db.Column(db.String(64))
