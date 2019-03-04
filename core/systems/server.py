import base64
import paramiko
import os

# Подключение к серверу
class Server:
    def __init__(self,host,user,password,**kwargs):
        self.host = host
        if 'ssh_open_key' in kwargs:
            with open(kwargs['ssh_open_key'],'r') as key:
                data = key.read().split(' ')[1]
                self.key=paramiko.RSAKey(data=base64.b64decode(bytes(data,'utf-8')))
        self.password=password
        self.user=user
        # self.connects_server()

    def connects_server(self,commands):
        print('Connections Server ....')
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # client.get_host_keys().add(self.host,'ssh-rsa',self.key)
        client.connect(self.host,username=self.user,password=self.password)
        for comm in commands:
            stdin, stdout, stderr = client.exec_command(comm)
            znak = 'w'
            if os.path.isfile('log/stdout.log'):
                znak = 'a'
            for line in stdout:
                with open('log/stdout.log',znak) as f:
                    f.write('... ' + line + '\n')
            for line in stderr:
                with open('log/error.log',znak) as f:
                    f.write('... ' + line + '\n')
        client.close()