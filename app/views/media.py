from flask import render_template

from app.src.utils import get_content_dir, get_dir_up, get_end_path
from app.src.utils import get_previous_file, get_next_file
from app.src.utils import get_files, get_content
from app.src.format import info_media

from . import views


@views.route('/media/<path:path>')
def render_media(path):

    info = info_media
    up = get_dir_up(path)
    title = get_end_path(path)

    data = get_content_dir(path.replace('/'+title, ''))
    data = get_files(data)
    content = get_content(data, title)

    # select template for file type
    template = '404.html'

    if content is not None:
        if content[3] == 'image':
            template = 'media_image.html'
        if content[3] == 'vector':
            template = 'media_image.html'
        if content[3] == 'sound':
            template = 'media_sound.html'
        if content[3] == 'video':
            template = 'media_video.html'
        if content[3] == 'docs':
            template = 'media_docs.html'

    # info media
    info['current'] = title
    info['previous'] = get_previous_file(data, title)
    info['next'] = get_next_file(data, title)

    return render_template(
        template,
        up=up,
        title=title,
        path=path,
        info=info,
        content=content,
        )
