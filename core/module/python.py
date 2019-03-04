def PythonModule(commands,i):
    if 'package' in i:
        commands = pipInstall(commands,i, i)

    commands.append('cd {}'.format(i['venv-settings']['src']))
    if i['name'] == 'python2':
        venv = 'virtualenv'
    else:
        venv = 'venv'
    commands.append('{} -m {} {}'.format(i['name'],venv,i['venv-settings']['src']+i['venv-settings']['name']))
    commands.append('source {}'.format(i['venv-settings']['src'] + i['venv-settings']['name'] + '/bin/activate'))

    if 'package' in i['venv-settings']:
        commands = pipInstall(commands,i['venv-settings'],i)

    return commands

def pipInstall(commands,venv,i):
    for pip_key in venv['package'].keys():
        if i['package'][pip_key] == 0:
            commands.append('pip install {}'.format(pip_key))
        else:
            commands.append('pip install {}=={}'.format(pip_key, i['package'][pip_key]))
    return commands