import os

from utils.logging import UtilLogging
from utils.command import UtilCommand
from utils.prompt import UtilPrompt
from utils.file import UtilFile

# Constants
SERVICE_NAME = "Clone repositories"
DESCRIPTION = "TBD"
URL_CLONE_PATH = "/Users/ssegura/Documents/Workplaces/reports_toolkit/cloned"
FILE_WITH_URLS = "/Users/ssegura/Documents/Workplaces/reports_toolkit/inputs/repos.txt"


class ServiceCloneRepositories:
    def get_url_parts(self, url):
        url_part_list = url.split("/")
        return {
            "protocol": url_part_list[0],
            "domain": url_part_list[2],
            "organization": url_part_list[3],
            "repository": url_part_list[4],
        }

    def format_url(self, url_parts):
        return "git@{domain}:{organization}/{repository}.git".format(**url_parts)

    def clone_repo(self, url, url_parts):
        # Services definition
        command = UtilCommand()
        file = UtilFile()

        file.check_if_path_exist(f"{URL_CLONE_PATH}/{url_parts['organization']}")
        command = f"cd {URL_CLONE_PATH}/{url_parts['organization']}; git clone {url} >/dev/null 2>&1"
        os.system(command)

    def run(self):
        # Services definition
        command = UtilCommand()
        prompt = UtilPrompt()
        file = UtilFile()
        log = UtilLogging()

        prompt.welcome("Clone Repositories")
        command.open(FILE_WITH_URLS)
        prompt.wait("Please fill the repository list file")
        repo_url_list = file.read_text_file_as_list(FILE_WITH_URLS)
        prompt.message(f"Found {len(repo_url_list)} repositoires in {FILE_WITH_URLS}")
        log.info("Process started")

        for url in repo_url_list:
            try:
                url_parts = self.get_url_parts(url)
                log.trace("Start clonning "+url_parts["repository"])
                url = self.format_url(url_parts)
                self.clone_repo(url, url_parts)
                log.trace("End clonning "+url_parts["repository"])
            except Exception as ex:
                log.error("During the cloning process "+str(ex))

        file.clear_file_content(FILE_WITH_URLS)
        log.info("The process finished successful")
        command.open(URL_CLONE_PATH)
