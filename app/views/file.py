from flask import send_from_directory

from app.src.utils import STORAGE_DIR
from . import views


@views.route('/file/<path:filename>')
def send_file(filename):
    return send_from_directory(STORAGE_DIR, filename)
