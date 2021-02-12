import os

DOCUMENTS = os.getenv('HOME')
DOCUMENTS += '/Documentos/'


def get_end_path(path):

    if(path.endswith("/") and len(path) > 1):
        path = path.rstrip('/')

    if('/' in path):
        title = path.split('/')
        title = title[len(title)-1]
    else:
        title = path

    return title


def get_content_dir(path):

    if (path != '/'):
        path = str(DOCUMENTS + path)
        if (os.path.exists(path)):
            content = os.listdir(path)
        else:
            content = None
    else:
        content = os.listdir(DOCUMENTS)

    if(content is not None):
        content.sort()
        content = sort_by_type(content, path)

    return content


def sort_by_type(content, path):

    dirs = []
    files = []

    if path == '/':
        path = DOCUMENTS
    else:
        path += '/'
        print(path)

    for item in content:
        if os.path.isdir(path + item):
            dirs.append(item)

    for item in content:
        if os.path.isfile(path + item):
            files.append(item)

    return dirs + files


def get_dir_up(path):

    if '/' in path and len(path) > 1:
        up = "/storage"
        path = path.split('/')
        size = len(path) - 1

        for i in range(size):
            up += '/'
            up += path[i]
    else:
        up = '/'

    return up


def get_pages(data):

    pages = [[]]
    void = []
    index = 0
    i = 0
    x = 0

    for item in data:
        data_type = 'dir'
        if '.' in item:
            data_type = 'file'

        if i == 24:
            i = 0
            x = x+1
            pages.append(list(void))
        pages[x].append([index, item, data_type])
        index += 1
        i += 1

    return pages


def get_content_page(pages):

    page = []

    for item in pages:
        page.append(item[1])

    return page
