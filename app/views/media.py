# from flask import render_template ,request

from . import views


@views.route('/media/<path:path>')
def render_media(path):

    return f"media {path}"
