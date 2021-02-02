from flask import render_template

from app.src.utils import get_content_dir, get_pages
from . import views


@views.route('/')
def index():

    data = get_content_dir('/')
    pages = get_pages(data)
    data = pages[0]

    info = {
        'first': 0,
        'current': 0,
        'finally': 0,
        'previous': None,
        'next': None
    }

    return render_template(
        'index.html',
        data=data,
        path='/',
        title='Home',
        info=info)
