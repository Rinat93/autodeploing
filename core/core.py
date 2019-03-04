from .module import LinuxModule,PythonModule
from .systems.server import Server
import json
class Core:

    def __init__(self,folder,files):
        self.folders = folder
        self.files = files
        self.parse_folder()
        self.server = None

    # Парсим папку с конфигами и берем все файлы
    def parse_folder(self):
        for i in self.files:
            if i.split('.')[-1] == 'json':
                self.open_config(self.folders+i)

    # Парсим файл конфигурации
    def open_config(self,file):
        with open(file,'r') as f:
            data = f.read()
        data = json.loads(data)
        self.server = Server(data['server']['host'],data['server']['user'],data['server']['password'],ssh_open_key=data['server']['ssh_open_key'])
        self.install_package(data)

    # Собираем комманды и кидаем на сервер запросы
    def install_package(self,data):
        if self.server != None:
            commands = []
            commands.append('apt update')
            for i in data['install']:
                if 'version' in i:
                    commands.append('apt -y install {}={}'.format(i['name'],i['version']))
                else:
                    commands.append('apt -y install {}'.format(i['name']))
                if 'module' in i:
                    if i['module'].lower() == 'python':
                        commands=PythonModule(commands,i)
                        if 'project' in i['venv-settings']:
                            commands = self.git(i['venv-settings']['project'], commands)
                            commands.append('pip install -r {}'.format(i['venv-settings']['project']['package']))

            if 'git' in data:
                commands = self.git(data,commands)

            self.server.connects_server(commands)

    # Форматируем комманду для клонирования с git'а
    def git(self,data,commands):
        if type(data['git']) != list:
            data['git'] = [data['git']]
        for i in data['git']:
            i['password'] = i['password'].replace('@', '%40')
            commands.append('git clone https://{} {}'.format(i['user'] + ':' + i['password'] + '@' + i['src'], i['local']))
        return commands