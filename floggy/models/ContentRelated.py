from sqlalchemy.dialects.postgresql import UUID

from floggy import db


class ContentRelated(db.Model):
    __tablename__ = 'content_related'

    id = db.Column(UUID(), primary_key=True)
    content_id = db.Column(UUID(), db.ForeignKey('contents.id'), index=True)
    to_content_id = db.Column(UUID(), db.ForeignKey('contents.id'))
