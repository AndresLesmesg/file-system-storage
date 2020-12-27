from flask import Blueprint


views = Blueprint('views', __name__, static_folder="templates")

from . import index
