from flask import Blueprint
from os import getenv


DOCUMENTS = getenv('HOME')
DOCUMENTS += '/Documentos'

views = Blueprint('views',
                  __name__,
                  static_folder="static",
                  template_folder="templates")

from . import index, storage, media, update, file
