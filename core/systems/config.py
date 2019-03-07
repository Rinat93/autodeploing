install_conf = {
    'name':'',
    'version': '',
    'venv':'',
}

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