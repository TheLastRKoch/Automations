import subprocess
import os


class UtilCommand:
    def open(self, path):
        os.system(f'open "{path}"')

    def run(self, cmd, path=os.getcwd()):
        return os.popen(f"cd {path}; {cmd} >/dev/null 2>&1").read()

    def background(self, cmd, path=os.getcwd()):
        os.system(f"cd {path}; {cmd} >/dev/null 2>&1")

    def clear(self):
        subprocess.call("clear")
