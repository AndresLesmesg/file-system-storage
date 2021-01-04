from os import getenv

DIR = getenv('HOME')
DIR += '/Documentos/'


class Config():
    SECRET_KEY = 'secret value'
    DEBUG = True
