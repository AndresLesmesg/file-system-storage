import os

DOCUMENTS = os.getenv('HOME')
DOCUMENTS += '/Documentos/'


def get_title(path):

    if(path.endswith("/") and len(path) > 1):
        path = path.rstrip('/')

    if('/' in path):
        title = path.split('/')
        title = title[len(title)-1]
    else:
        title = path

    return title


def get_content(path):
    if (path != '/'):
        path = str(DOCUMENTS + path)
        if (os.path.exists(path=path)):
            data = os.listdir(path)
        else:
            data = 'error value'
    else:
        data = os.listdir(DOCUMENTS)
    if(data is not None):
        data.sort()

    return data


def get_dir_up(path):

    if '/' in path:
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


def get_info_page(title, path, data):
    pass
