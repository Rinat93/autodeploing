from .module import LinuxModule,modules_run,git
from .systems.server import Server
from .systems.config import settings_conf
from .systems.ftp import ftp_upload
import json
import asyncio
import threading
class Core:

    def __init__(self,folder,files,**kwargs):
        if 'arch' in kwargs:
            os = kwargs['os']
        else:
            os = 'debian'
        self.folders = folder
        self.files = files
        self.os_command = settings_conf[os]
        self.parse_folder()
        self.server = None

    # Парсим папку с конфигами и берем все файлы
    def parse_folder(self):
        futures = []
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        for i in self.files:
            if i.split('.')[-1] == 'json':
                futures.append(self.open_config(self.folders+i))
        loop.run_until_complete(asyncio.wait(futures))
        loop.close()

    # Парсим файл конфигурации
    async def open_config(self,file):
        with open(file,'r') as f:
            data = f.read()
        data = json.loads(data)
        # if 'ftp' in data:
        #     self.ftp_init(data['ftp'],data['server'])
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