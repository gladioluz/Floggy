from werkzeug.routing import BaseConverter, ValidationError
import uuid
import re

UUID_RE = re.compile(
    r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
)


class UUIDConverter(BaseConverter):
    def to_python(self, value):
        if not UUID_RE.match(value):
            raise ValidationError

        try:
            uuid.UUID(value)
        except ValueError:
            raise ValidationError

        return value

    def to_url(self, value):
        return value
