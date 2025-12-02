import subprocess


class ServiceCleanClipboard:
    def run_copyq_command(self, command):
        """Run a copyq command and capture its output."""
        try:
            output = subprocess.check_output(
                command, stderr=subprocess.STDOUT, shell=True
            ).decode("utf-8")
            return output
        except subprocess.CalledProcessError as e:
            return e.output.decode("utf-8")

    def run(self):
        copyq_status = self.run_copyq_command('copyq copy "test"')

        if "Start CopyQ server first" in copyq_status:
            print("Error: fail to clean the clipboard. CopyQ server is not running")
        else:
            print("Cleaning clipboard")
            for _ in range(62):
                subprocess.run('copyq add ""', shell=True)
