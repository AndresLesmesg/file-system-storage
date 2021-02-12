from flask import render_template, request, redirect, url_for, flash

from app.src.utils import get_end_path, get_dir_up, get_content_dir
from app.src.utils import get_pages
from . import views


@views.route('/storage/<path:path>', methods=['GET', 'POST'])
def content(path):

    up = get_dir_up(path)

    if request.method == 'POST':

        return redirect(url_for('update', path))

    if('.' in path):
        # redirect to doctype
        if('pdf' in path or 'PDF' in path):

            title = get_end_path(path)

            return render_template(
                'media_doctype.html',
                title=title,
                path=path)

        # redirect to image
        if('png' in path or 'jpg' in path or 'PNG' in path or 'JPG' in path):

            title = get_end_path(path)
            data = get_content_dir(get_dir_up(path))

            # Control-nav-items
            info = {
                'current-file': title,
                'previous-file': None,
                'next-file': None,
            }

            current_id = 0

            i = 0

            for item in data:

                if item == title:
                    current_id = i
                i += 1

            if current_id is not None:
                if current_id > 0:
                    info['previous-file'] = data[current_id - 1]
                if current_id < len(data) - 1:
                    info['next-file'] = data[current_id + 1]

            return render_template(
                'media_image.html',
                up=up,
                path=path,
                info=info,
                title=title)
    else:

        title = get_end_path(path)
        data = get_content_dir(path)
        pages = get_pages(data)

        # Pagination
        if len(pages) > 1:

            info = {
                'first': 0,
                'current': 0,
                'finally': len(pages) - 1,
                'previous': None,
                'next': None
            }

            if request.method == 'GET':

                if request.args.get('page') is not None:

                    try:
                        page = int(request.args.get('page'))
                    except ValueError:
                        flash('error', 'numero de pagina no valida')

                    if page < len(pages):
                        info['current'] = page

                        if info['current'] != 0:
                            info['previous'] = info['current'] - 1

                        if info['current'] != info['finally']:
                            info['next'] = info['current'] + 1

                if info['current'] == 0:
                    if info['current'] != 0:
                        info['previous'] = info['current'] - 1

                    if info['current'] != info['finally']:
                        info['next'] = info['current'] + 1

        else:

            info = {
                'first': 0,
                'current': 0,
                'finally': 0,
                'previous': None,
                'next': None
            }

        data = pages[info['current']]

        return render_template(
            'index.html',
            up=up,
            path=path,
            title=title,
            info=info,
            data=data)
