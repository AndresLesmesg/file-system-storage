from app.src.format import type_file_list

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


def get_clean_path(path):

    if '%' in path:
        clean_path = path
        clean_path = clean_path.replace('%20', ' ')
        clean_path = clean_path.replace('%26', '&')
        clean_path = clean_path.replace('%28', '(')
        clean_path = clean_path.replace('%29', ')')
        clean_path = clean_path.replace('%2B', '+')
    else:
        clean_path = path

    return clean_path


def is_path_exist(path):
    path = os.path.join(STORAGE_DIR, path)
    if(os.path.exists(path)):
        return True

    return False


def is_file(path):
    path = os.path.join(STORAGE_DIR, path)
    if(os.path.isfile(path)):
        return True

    return False


def get_content_dir(path):
    content = None
    if(path == '/'):
        dir = STORAGE_DIR
        content = os.listdir(dir)

    else:
        dir = os.path.join(STORAGE_DIR, path)
        if(os.path.exists(dir)):
            content = os.listdir(dir)

    if(content is not None):
        content.sort()
        content = sort_by_type(content, dir)
        content = add_index_content(content)

    return content


def add_index_content(content):
    for x in range(len(content)):
        content[x].insert(0, x)
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
            dirs.append([item, 'dir'])

    for item in content:
        if os.path.isfile(path + item):
            files.append([item, 'file', add_ext_file(item)])

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
    i = 0
    x = 0

    for item in data:
        if i == 24:
            pages.append(list(void))
            x = x + 1
            i = 0
        pages[x].append([x, item])
        i += 1

    data = []
    return pages


def add_ext_file(data):
    if data.startswith('.'):
        return 'hidden'
    for ext_list in type_file_list:
        for ext in type_file_list[ext_list]:
            if(data.lower().endswith(ext)):
                return ext_list

    return 'undefined'


def get_files(data):
    files = []
    for item in data:
        if item[2] == 'file':
            files.append(item)

    return files


def get_next_file(data, filename):
    file = False
    for item in data:
        if file and (item[3] != 'undefined' and item[3] != 'hidden'):
            return item[1]
        if item[1] == filename:
            file = True
    return None


def get_previous_file(data, filename):
    file = ''
    for item in data:
        if item[1] == filename:
            return file
        if(item[3] != 'undefined' and item[3] != 'hidden'):
            file = item[1]
    return None


def get_content(data, filename):
    for item in data:
        if item[1] == filename:
            return item
    return None
