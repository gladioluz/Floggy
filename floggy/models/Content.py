from sqlalchemy.dialects.postgresql import UUID

from floggy import db


class Content(db.Model):
    __tablename__ = 'contents'

    id = db.Column(UUID(), primary_key=True)
    uri = db.Column(db.String(64), unique=True, index=True)
    content_type_id = db.Column(UUID(), db.ForeignKey('content_types.id'),
                                index=True)
    rubric_id = db.Column(UUID(), db.ForeignKey('rubrics.id'), index=True)
    user_id = db.Column(UUID(), db.ForeignKey('users.id'), index=True)
    title_seo = db.Column(db.String(64))
    description_seo = db.Column(db.String(160))
    preview = db.Column(db.String(128))
    alt = db.Column(db.String(64))
    content_image = db.Column(db.String(128))
    language_seo = db.Column(db.String(2))
    title = db.Column(db.String(128))
    description = db.Column(db.Text())
    body = db.Column(db.Text())

    rating = db.Column(db.Integer(), default=0)
    seen = db.Column(db.Integer(), default=0)
    comment_count = db.Column(db.Integer(), default=0)

    created = db.Column(db.DateTime())
    updated = db.Column(db.DateTime())

    status = db.Column(db.SmallInteger())
