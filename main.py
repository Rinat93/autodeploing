import os
from core.core import Core

if __name__ == '__main__':

    if os.path.isdir('./conf'):
        Core('./conf/', os.listdir('./conf'))
    else:
        Exception("Ошибка, нет папки conf")