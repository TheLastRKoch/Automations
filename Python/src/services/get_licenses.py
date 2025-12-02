from urllib import parse
import jmespath
import json
import re

from utils.webrequest import UtilWebRequest
from utils.logging import UtilLogging
from utils.command import UtilCommand
from utils.file import UtilFile

INPUT_FILE_PATH = "/Users/ssegura/Documents/Workplaces/reports_toolkit/components.xlsx"
PACKAGE_MANAGER_MAPPING = {"gem": {"name": "Ruby Gems", "url": "https://rubygems.org/api/v1/gems/{package_name}.json?version={version}", "pattern": "licenses | join('& ',@)"}, "npm": {"name": "JavaScript NPM", "url": "https://registry.npmjs.org/{package_name}/{version}", "pattern": "license"}, "pypi": {
    "name": "Python Pypi", "url": "https://pypi.org/pypi/{package_name}/{version}/json", "pattern": "info.license"}, "golang": {"name": "Golang pkg", "url": "https://api.deps.dev/v3alpha/systems/go/packages/{package_name}/versions/{version}", "pattern": "licenses | join('& ',@)"}}
PATTERN_GET_KEYWORD = r"pkg:(.+?)\/"
CMD_OPEN_FILE = "open {path}"
SHEET_NAME = "components"


class ServiceGetLicenses:
    def get_license(self, url, pattern):

        # Init services
        service_request = UtilWebRequest()

        r = service_request.get(url=url)
        if r.status_code // 10 != 20:
            # log an error
            return "N/A"
        json_body = json.loads(r.text)
        query = jmespath.compile(pattern)
        return query.search(json_body)

    def run(self):

        # Init utils
        command = UtilCommand()
        logging = UtilLogging()
        file = UtilFile()

        # Open input file
        command.background(CMD_OPEN_FILE.format(path=INPUT_FILE_PATH))
        command.clear()
        input("Please press any key to continue\n")
        command.clear()
        logging.info("Process started")

        # Open CSV
        xlsx_file = file.read_excel(INPUT_FILE_PATH, SHEET_NAME)

        # For each row in the CSV
        for idx, row in xlsx_file.iterrows():
            try:
                logging.info(f"Start procesing {row['Organization']} {row['Repository']} {row['Name']}")
                # Identify the type of package
                purl = row["Purl"]
                keyword = re.search(PATTERN_GET_KEYWORD, purl).group(1)

                package_name = row["Name"]
                package_version = row["Version"]

                if (keyword == "golang"):
                    package_name = parse.quote(package_name, safe="")

                url = PACKAGE_MANAGER_MAPPING[keyword]["url"].format(
                    package_name=package_name,
                    version=package_version
                )
                name = PACKAGE_MANAGER_MAPPING[keyword]["name"]
                pattern = PACKAGE_MANAGER_MAPPING[keyword]["pattern"]
                logging.trace("Found package manager "+name)
                license = self.get_license(url, pattern)
                if license == "":
                    license = "N/A"
            except Exception as ex:
                logging.error("Someting went wrong during the license fetching process: "+str(ex))
                license = "N/A"
            finally:
                xlsx_file.loc[idx, "Licenses"] = license
                logging.info(f"End procesing {row['Organization']} {row['Repository']} {row['Name']}")

        file.write_excel(INPUT_FILE_PATH, SHEET_NAME, xlsx_file)
        command.background(CMD_OPEN_FILE.format(path=INPUT_FILE_PATH))
        logging.info("Process finished")
