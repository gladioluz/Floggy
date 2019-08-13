from flask_login import current_user
from functools import wraps
from floggy import login


def login_required(roles=["ANY"]):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if current_user.is_anonymous:
                return login.unauthorized()
            if (current_user.role not in roles) and (roles != "ANY"):
                return login.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
