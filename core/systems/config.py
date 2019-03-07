import os
install_conf = {
    'name':'',
    'version': '',
    'venv':'',
}

# Параметры которые передаются аргументами
application_conf = {
    'os': os.environ.get('os'),
    'serv': os.environ.get('serv')
}

# Настройка для ОС
settings_conf = {
    'debian': {
        'command': 'apt',
        'update': 'update',
        'upgrade': 'upgrade',
        'install': 'install'
    },
    'ubuntu': {
        'command': 'apt',
        'update': 'update',
        'upgrade': 'upgrade',
        'install': 'install'
    },
    'arch': {
        'command': 'pacman',
        'update': '-Sy',
        'upgrade': '-Syu',
        'install': '-S'
    }
}