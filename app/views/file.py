from flask import send_from_directory

from .utility import DOCUMENTS
from . import views


@views.route('/file/<path:filename>')
def send_file(filename):
    return send_from_directory(DOCUMENTS, filename)
