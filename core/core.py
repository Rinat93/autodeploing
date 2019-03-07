from .module import LinuxModule,modules_run,git
from .systems.server import Server
from .systems.config import *
from .systems.ftp import ftp_upload
import json
import asyncio

class Core:

    def __init__(self,folder,files,**kwargs):

        if application_conf['os'] == None:
            application_conf['os'] = 'debian'

        if application_conf['serv'] != None:
            self.files = [i+'.json' for i in application_conf['serv'].split(',') if i.endswith('.json')==False]
        else:
            self.files = files

        self.folders = folder
        self.os_command = settings_conf[application_conf['os']]
        self.parse_folder()
        self.server = None

    # Парсим папку с конфигами и берем все файлы
    def parse_folder(self):
        futures = []

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        for i in self.files:
            if i.endswith('.json'):
                if os.path.isfile(self.folders+i):
                    futures.append(self.open_config(self.folders+i))
                else:
                    raise Exception("Не найден файл: "+self.folders+i)
        loop.run_until_complete(asyncio.wait(futures))
        loop.close()

    # Парсим файл конфигурации
    async def open_config(self,file):
        with open(file,'r') as f:
            data = f.read()
        data = json.loads(data)
        if 'ftp' in data:
            await self.ftp_init(data['ftp'],data['server'])
        self.server = Server(data['server']['host'],data['server']['user'],data['server']['password'],ssh_open_key=data['server']['ssh_open_key'])
        await self.install_package(data)

    # FTP connect
    async def ftp_init(self, ftp,server):
        for i in ftp:
            await ftp_upload(i['src'], i['to'],server)

    # Собираем комманды и кидаем на сервер запросы
    async def install_package(self,data):
        if self.server != None:
            commands = []
            commands.append('{} {}'.format(self.os_command['command'],self.os_command['update']))
            for i in data['install']:
                if 'version' in i:
                    commands.append('{} -y {} {}={}'.format(self.os_command['command'],self.os_command['install'],i['name'],i['version']))
                else:
                    commands.append('{} -y {} {}'.format(self.os_command['command'],self.os_command['install'],i['name']))
                if 'module' in i:
                    commands = modules_run(commands,i)

            if 'git' in data:
                commands = git(data,commands)

            await self.server.connects_server(commands)