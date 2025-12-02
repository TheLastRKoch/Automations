from os import environ as env
import os


class UtilPrompt:
    
    def __show_pushup_notification(self, title, message):
        os.system("""
                osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "{}"'
                """.format(message, env["APPLICATION_NAME"], title, env["NOTIFICATIONS_SOUND"]))

    def info(self, title, message):
        self.__show_pushup_notification(title, message)

    def error(self, title, message):
        self.__show_pushup_notification("Error: "+title, message)
    
    def welcome(self, service_name):
        os.system("clear")
        print(f"Welcome to the service {service_name}")
        print("================================================\n\n")

    def press_key_continue(self):
        print("")
        print("================================================")
        print("          press any key to continue")
        input("================================================\n")
        os.system("clear")

    def clear(self):
        os.system("clear")

    def wait(self, body):
        os.system("clear")
        print(body)
        self.press_key_continue()

    def message(self, text):
        os.system("clear")
        print(text)