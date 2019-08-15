from flask import Blueprint

bp = Blueprint('admin_contents_bp', __name__)

from floggy.admin.components.contents import controllers
