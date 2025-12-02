from dotenv import load_dotenv
from os import environ as env
import jmespath
import json
import re

from services.service_logger import ServiceLogger as log
from services.service_prompt import ServicePrompt
from services.service_request import ServiceRequest
from services.service_files import ServiceFiles


NUM_PER_PAGE = 100
MAX_PAGE_NUM = 5

# Regex patterns
GET_ORG_NAME_PATTER = r"github\.{hostname}\.net\/(.+?)(?:$|\/$|\/.+?)"

# JMESPath Queries
FORMAT_REPO_LIST_QUERY = r"[*].html_url"

# URLS
BASE_GIT_URL = r"https://{hostname}/orgs/{org_name}/repos?per_page={num_per_page}&page={page_num}"

# Paths
REPO_LIST_PATH = r"/Users/ssegura/Documents/Workplaces/reports_toolkit/inputs/repo_list.txt"


def get_org_name(org_url):
    result = re.search(GET_ORG_NAME_PATTER, org_url)
    if not result.group(1):
        raise ("Error: the Organization name could not be found")
    return result.group(1)


def get_repo_list(org_name):
    repo_list = []

    headers = {"Authorization": "Bearer "+env["GITHUB_PAT"]}

    for page in range(1, MAX_PAGE_NUM+1):
        url = BASE_GIT_URL.format(
            org_name=org_name,
            num_per_page=NUM_PER_PAGE,
            page_num=page
        )
        request = service_request.get(url=url, headers=headers)
        items = json.loads(request.text)
        if len(items) == 0:
            return repo_list
        repo_list = repo_list + items
    return repo_list


def format_repo_list(repo_list):
    query = jmespath.compile(FORMAT_REPO_LIST_QUERY)
    return query.search(repo_list)


def generate_report(repo_list):
    service_file = ServiceFiles()

    service_file.clean_textfile
    service_file.write_textfile(REPO_LIST_PATH, "\n".join(repo_list))
    service_file.open_file(REPO_LIST_PATH)


if __name__ == "__main__":
    # load env variables
    load_dotenv()

    # Init services
    service_request = ServiceRequest()
    service_prompt = ServicePrompt()

    service_prompt.clear()
    org_url = service_prompt.question("Please type the GitHub organization URL from which you want to obtain the repository list")
    org_name = get_org_name(org_url)
    log.info("Process started")
    log.info("Start processing "+org_name)
    raw_repo_list = get_repo_list(org_name)
    log.info(f"Found {len(raw_repo_list)} repositories on {org_name}")
    repo_list = format_repo_list(raw_repo_list)
    generate_report(repo_list)

    log.info("Process finished")
