class LinuxModule:

    def __init__(self,os,**kwargs):
        self.os = os

    def command_install(self):

        commands = {
            'debian': 'apt',
            'ubuntu': 'apt'
        }