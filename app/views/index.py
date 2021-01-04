from flask import render_template

from .utility import get_content, get_pages
from . import views


@views.route('/')
def index():

    data = get_content('/')
    pages = get_pages(data)
    data = pages[0]

    info = {
        'first': 0,
        'current': 0,
        'finally': 0,
        'previous': None,
        'next': None
    }

    return render_template('index.html', data=data, path='/', title='Home', info=info)
