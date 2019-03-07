from .python import PythonModule

# Смотрим что за модуль и подключаем доп "возможности"
def modules_run(commands,i):
    if i['module'].lower() == 'python':
        commands = PythonModule(commands, i)
        if 'project' in i['venv']:
            commands = git(i['venv']['project'], commands)
            commands.append('pip install -r {}'.format(i['venv']['project']['package']))

    return commands

# Форматируем комманду для клонирования с git'а
def git(data,commands):
    if type(data['git']) != list:
        data['git'] = [data['git']]
    for i in data['git']:
        i['password'] = i['password'].replace('@', '%40')
        commands.append('git clone https://{} {}'.format(i['user'] + ':' + i['password'] + '@' + i['src'], i['local']))
    return commands