from flask import render_template, request, redirect, url_for, flash

from app.src.utils import get_end_path, get_dir_up, get_clean_path
from app.src.utils import get_content_dir, get_pages
from app.src.format import imgs_type_file
from . import views


@views.route('/storage/<path:path>', methods=['GET', 'POST'])
def content(path):

    up = get_dir_up(path)
    title = get_end_path(path)

    if request.method == 'POST':

        return redirect(url_for('update', path))

    if('.' in title):
        # redirect to doctype
        return redirect(f'/media/{path}')

    else:

        # clear url encoding

        clean_path = get_clean_path(path)
        data = get_content_dir(clean_path)
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
            img=imgs_type_file,
            title=title,
            info=info,
            data=data)
