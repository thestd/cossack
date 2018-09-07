"""
TODO:
- MANAGE NGINX
- MANAGE SUPERVISOR
- DEACTIVATE/ACTIVATE FIREWALL
- PROJECT DEPLOY
- MIGRATION RUN
- EXEC COMMAND
"""

import os
import settings as set
from subprocess import *

class OS:
    def runner(self, cmd, return_result=False):
        try:
            if not return_result:
                Popen(cmd, shell=True)
            else:
                res = check_output(cmd, shell=True)
        except Exception as e:
            return e.args
        else:
            if return_result:
                return res.decode("utf-8")
            return 0

    def sudo(self, password, run=False):
        cmd = f"echo {password} | sudo -S "
        if not run:
            return cmd
        return self.runner(cmd, return_result=True)

    def service(self, tool, action, run=False):
        cmd = f"service {tool} {action}"
        if not run:
            return cmd
        return self.runner(cmd, return_result=True)

    def ls(self, run=True):
        cmd = "ls"
        if not run:
            return cmd
        return self.runner(cmd, return_result=True)

    def pwd(self, run=True):
        cmd = "pwd"
        if not run:
            return cmd
        return self.runner(cmd, return_result=True)

    def __str__(self):
        cmd = "uname -a"
        return str(self.runner(cmd, return_result=True))

    def __call__(self, *args, **kwargs):
        cmd = "uname -a"
        return str(self.runner(cmd, return_result=True))


class Nginx(OS):
    def start(self):
        cmd = f"{self.sudo(set.SUDO_PASSWD)}{self.service('nginx', 'start')}"
        return self.runner(cmd)

    def restart(self):
        cmd = f"{self.sudo(set.SUDO_PASSWD)}{self.service('nginx', 'restart')}"
        return self.runner(cmd)

    def stop(self):
        cmd = f"{self.sudo(set.SUDO_PASSWD)}{self.service('nginx', 'stop')}"
        return self.runner(cmd)

    def status(self):
        cmd = f"{self.sudo(set.SUDO_PASSWD)}{self.service('nginx', 'status')}"
        return self.runner(cmd, return_result=True)

    def __str__(self):
        return self.status()

    def __call__(self, *args, **kwargs):
        return self.start()


class Supervisor(OS):
    def __init__(self):
        pass

    def start(self):
        pass

    def restart(self):
        pass

    def stop(self):
        pass

    def __str__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


nx = Nginx()
os = OS()

nx.status()