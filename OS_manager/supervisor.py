from .os import OS
import settings as sett


class Supervisor(OS):
    def start(self, app=''):
        cmd = f"{self.sudo(sett.SUDO_PASSWD)}supervisorctl start {app}"
        return self.runner(cmd)

    def restart(self, app=''):
        cmd = f"{self.sudo(sett.SUDO_PASSWD)}supervisorctl restart {app}"
        return self.runner(cmd)

    def stop(self, app=''):
        cmd = f"{self.sudo(sett.SUDO_PASSWD)}supervisorctl stop {app}"
        return self.runner(cmd)

    def pid(self, app=''):
        cmd = f"{self.sudo(sett.SUDO_PASSWD)}supervisorctl pid {app}"
        return self.runner(cmd)

    def __str__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass
