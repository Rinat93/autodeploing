import os
from core.core import Core

if __name__ == '__main__':
    dir_conf = './conf/'

    if os.environ.get('dir') != None:
        dir_conf = os.environ.get('dir')

    if os.path.isdir(dir_conf):
        Core(dir_conf, os.listdir(dir_conf))
    else:
        raise Exception("Ошибка, нет папки {}".format(dir_conf))