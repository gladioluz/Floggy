from flask import Blueprint

bp = Blueprint('admin_tags_bp', __name__)

from floggy.admin.components.tags import controllers
