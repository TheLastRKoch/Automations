import time
import schedule

from utils.logging import UtilLogging
from utils.command import UtilCommand
from utils.prompt import UtilPrompt

COMMAND_NAME = "Auth dev server"
COMMAND = r'shortcuts run "Auth Demark server"'
FREQUENCY = 30


class ServiceScheduleTask:
    def __init__(self):
        # Init utils
        self.log = UtilLogging()
        self.cmd = UtilCommand()
        self.promt = UtilPrompt()

    def execute_task(self):
        self.cmd.run(COMMAND)
        self.log.info("Executed "+COMMAND_NAME)

    def run(self):
        try:
            schedule.every(FREQUENCY).minutes.do(self.execute_task)
            self.promt.clear()
            self.log.info("Process started")
            while True:
                schedule.run_pending()
                # Sleep for a second to avoid busy waiting
                time.sleep(1)

        except KeyboardInterrupt:
            self.log.info("Process finished")

        except Exception as e:
            self.log.error("Something happened with the task: "+str(e))
