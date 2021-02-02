from flask import request, flash
from werkzeug.utils import secure_filename
from app.src.utils import DOCUMENTS
from . import views


@views.route('/update/<path:path>', methods=['POST'])
def update_sotrage(path):

    if request.method == 'POST':
        file = request.files['the_file']
        file.save(DOCUMENTS + path + '/' + secure_filename(file.filename))
        flash(
            'message',
            "the file '{}' was saved in {} ".format(file.name, path))
