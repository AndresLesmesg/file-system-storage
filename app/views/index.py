import os
import json
from flask import render_template

from . import views

DOCUMENTS = os.getenv('HOME')
DOCUMENTS += '/Documentos'

def list_content(path):
    if (path != '/'):
        path = str(DOCUMENTS + '/' + path)
        if (os.path.exists(path=path)):
            data = os.listdir(path)
        else:
            data = 'error value'
    else:
        data = os.listdir(DOCUMENTS)
    print(type(data))
    print(data)
    data = data.split(',')
    data = list(json.dumps(data))
    print(type(data))
    print(data)
    return data


def check_file(parameter_list):
    """
    docstring
    """
    pass

@views.route('/')
def index():
    data = list_content('/')

    return render_template('index.html', info=data, title='Home')
    

@views.route('/<path:path>')
def content(path):

    if('.' in path):
        if('pdf' in path or 'PDF' in path):
            return "pdf \n {}".format(list_content(path))
        if('png' in path or 'jpg' in path or 'PNG' in path or 'JPG' in path):
            return "image \n {}".format(list_content(path))
    else:    
        return "tree: \n {}".format(list_content(path))


@views.route('/<path>', methods=['GET','POST'])
def add_content(path):

    if('.' in path):
        if('pdf' in path or 'PDF' in path):
            return "pdf"
        if('png' in path or 'jpg' in path or 'PNG' in path or 'JPG' in path):
            return "image"
    else:
        return "tree"