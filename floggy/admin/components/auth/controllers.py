from flask import (
    request,
    render_template,
)

from floggy import recaptcha
from floggy.admin.components.auth import bp
from floggy.admin.components.auth.forms import LoginForm


@bp.route('/admin')
def admin_auth():
    pass
