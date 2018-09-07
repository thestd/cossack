from .os import OS


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
