from utils.command import UtilCommand
from utils.prompt import UtilPrompt
from utils.file import UtilFile

from os import environ as env


class ServiceOpenURLList:
    def remove_duplicates(self, url_list):
        return list(dict.fromkeys(url_list))

    def remove_void_items(self, url_list):
        return list(filter(lambda a: a.strip() != "", url_list))

    def open_urls(self, url_list):
        command = UtilCommand()

        limit = int(env["URL_PER_TIME"])
        count = 1
        for idx, url in enumerate(url_list):
            if count == limit:
                input(
                    f"{idx+1}/{len(url_list)} URLs opened press any key to continue"
                )
                count = 0
            command.open(url)
            count = count + 1

    def run(self):
        # Service definition
        prompt = UtilPrompt()
        files = UtilFile()

        url_path = env["URL_LIST_PATH"]
        prompt.welcome("Open URL list")
        files.open(url_path)
        prompt.wait("Please fill the URL list file")
        url_list = files.read_text_file_as_list(url_path)
        url_list = self.remove_duplicates(url_list)
        url_list = self.remove_void_items(url_list)
        prompt.message(f"Found {len(url_list)} unique URLs\n")
        self.open_urls(url_list)
        files.clear_file_content(url_path)
