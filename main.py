import os
from core.core import Core

if __name__ == '__main__':
    if os.path.isdir('./conf'):
        print("Папка есть")
        Core('./conf/', os.listdir('./conf'),os='arch')
    else:
        Exception("Ошибка, нет папки conf")