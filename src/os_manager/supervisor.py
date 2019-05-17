from .os_manager import OS
from src.config_parser import Config

config = Config()


class Supervisor(OS):
    def start(self, app=''):
        cmd = f"{self.sudo(config.os.sudo_password)}supervisorctl start {app}"
        return self.runner(cmd)

    def restart(self, app=''):
        cmd = f"{self.sudo(config.os.sudo_password)}supervisorctl restart {app}"
        return self.runner(cmd)

    def stop(self, app=''):
        cmd = f"{self.sudo(config.os.sudo_password)}supervisorctl stop {app}"
        return self.runner(cmd)

    def pid(self, app=''):
        cmd = f"{self.sudo(config.os.sudo_password)}supervisorctl pid {app}"
        return self.runner(cmd)

    def __str__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass
