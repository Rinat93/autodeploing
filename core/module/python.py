# Сборка команд для Python
def PythonModule(commands,i):
    if 'package' in i:
        commands = pipInstall(commands,i, i)

    commands.append('cd {}'.format(i['venv']['src']))
    if i['name'] == 'python2':
        venv = 'virtualenv'
    else:
        venv = 'venv'
    commands.append('{} -m {} {}'.format(i['name'],venv,i['venv']['src']+i['venv']['name']))
    commands.append('source {}'.format(i['venv']['src'] + i['venv']['name'] + '/bin/activate'))

    if 'package' in i['venv']:
        commands = pipInstall(commands,i['venv'],i)

    return commands

# Собираем команды для установки в виртуальное окружение пакетов
def pipInstall(commands,venv,i):
    for pip_key in venv['package'].keys():
        if i['package'][pip_key] == 0:
            commands.append('pip install {}'.format(pip_key))
        else:
            commands.append('pip install {}=={}'.format(pip_key, i['package'][pip_key]))
    return commands