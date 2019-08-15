from flask import Blueprint

bp = Blueprint('admin_auth_bp', __name__)

from floggy.admin.components.auth import controllers
