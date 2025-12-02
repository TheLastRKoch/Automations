from utils.webrequest import UtilWebRequest
from utils.prompt import UtilPrompt
from utils.file import UtilFile

from os import environ as env


class ServiceCheckURLList:
    def remove_duplicates(self, url_list):
        return list(dict.fromkeys(url_list))

    def remove_void_items(self, url_list):
        return list(filter(lambda a: a.strip() != "", url_list))

    def check_url_list(self, url_list):
        # Init Utils
        web_request = UtilWebRequest()

        for url in url_list:
            r = web_request.get(url=url)
            status_code = r.status_code
            print(f"[{status_code}]\t{url}")

    def run(self):
        # Service definition
        prompt = UtilPrompt()
        files = UtilFile()

        url_path = env["URL_LIST_PATH"]
        prompt.welcome("Check URL list")
        files.open(url_path)
        prompt.wait("Please fill the URL list file")
        url_list = files.read_text_file_as_list(url_path)
        url_list = self.remove_duplicates(url_list)
        url_list = self.remove_void_items(url_list)
        prompt.message(f"Found {len(url_list)} unique URLs\n")
        self.check_url_list(url_list)
        files.clear_file_content(url_path)
