from flask import request
# from flask import render_template, send_from_directory
from . import views


@views.route('/update/<path:path>', methods=['POST'])
def update_sotrage():
    """
    get request

    validate request

    save request

    send flash

    """
    pass
