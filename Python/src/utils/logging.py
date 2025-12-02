from datetime import datetime


class UtilLogging:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    LIGHTBLUE = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    UNDERLINE = '\033[4m'
    COMMON = '\033[0m'

    def __get_time_standard(self):
        return datetime.utcnow().strftime("%d/%b/%Y %H:%M:%S")

    def custom_log(self, message, level, color):
        timestamp = self.__get_time_standard()
        print(color, "{"+f" {timestamp} | {level} | {message} "+"}")

    def trace(self, message):
        self.custom_log(message, "Trace", self.UNDERLINE)

    def info(self, message):
        self.custom_log(message, "Info", self.COMMON)

    def alert(self, message):
        self.custom_log(message, "Warning", self.YELLOW)

    def error(self, message):
        self.custom_log("Error: "+message, "Error", self.RED)
