import base64
import asyncssh

# Подключение к серверу
class Server:
    def __init__(self,host,user,password,**kwargs):
        self.host = host
        if 'ssh_open_key' in kwargs:
            with open(kwargs['ssh_open_key'],'r') as key:
                data = key.read().split(' ')[1]

                self.key=asyncssh.rsa._RSAKey(base64.b64decode(bytes(data,'utf-8'))) #paramiko.RSAKey(data=base64.b64decode(bytes(data,'utf-8')))
        self.password=password
        self.user=user
        # self.connects_server()

    # Логирование
    async def log_files(self,out,type):
        with open('log/{}-ssh.log'.format(type), 'w') as f:
            text = ''
            for i in out['info']:
                text += i + '\n'
            f.write(text)

    # Коннект к серверу и выполнение комманд
    async def call_commands(self,commands):

        async with asyncssh.connect(host=self.host,username=self.user,password=self.password,known_hosts=None) as conn:
            out = {
                'err': [],
                'info':[]
            }
            for comm in commands:
                result = await conn.run(comm)
                out['err'].append(comm+ ' ---- ' +result.stderr)
                out['info'].append(comm+ ' ---- ' +result.stdout)

            await self.log_files(out,'stdout')
            await self.log_files(out,'error')


    async def connects_server(self,commands):
        print('Connections Server ....')
        await self.call_commands(commands)