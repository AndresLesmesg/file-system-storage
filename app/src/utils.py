import os

STORAGE_DIR = os.getenv('STORAGE_DIR')


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
    content = None
    if(path == '/'):
        content = os.listdir(STORAGE_DIR)
    else:
        dir = os.path.join(STORAGE_DIR, path)
        if(os.path.exists(dir)):
            content = os.listdir(dir)
            if(content is not None):
                content.sort()
                content = sort_by_type(content, dir)

    return content


def sort_by_type(content, path):

    dirs = []
    files = []

    if path == '/':
        path = STORAGE_DIR
    else:
        path += '/'

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
        pages[x].append([i, item, data_type])
        index += 1
        i += 1

    return pages


def get_content_page(pages):

    page = []

    for item in pages:
        page.append(item[1])

    return page
