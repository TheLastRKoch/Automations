from services.service_prompt import ServicePrompt
from services.service_files import ServiceFiles
import pandas


EXCLUSIONS = r"/Users/ssegura/Documents/Workplaces/reports_toolkit/inputs/exclusions.txt"
LEFT_JOIN = r"/Users/ssegura/Documents/Workplaces/reports_toolkit/inputs/left_join.xlsx"
SHEET_NAME = "Query"


def get_exclusion_dic():

    # Services
    service_files = ServiceFiles()

    # Initialization
    exclusion_dic_list = []

    exclusions = service_files.read_textfile(EXCLUSIONS)
    exclusion_rows = exclusions.split("\n")

    for row in exclusion_rows:
        exclusion_parts = row.split("\t")
        exclusion_dic_list.append({"name": exclusion_parts[0], "version": exclusion_parts[1]})

    return exclusion_dic_list


def remove_exclusions(exclusion_dic_list):
    excel_dt = pandas.read_excel(LEFT_JOIN, "Query")
    for exclusion in exclusion_dic_list:
        excel_dt = excel_dt.query(
            f'`OSS Name` != \'{exclusion["name"]}\' and `Package Version` != \'{exclusion["version"]}\'')
    return excel_dt


if __name__ == "__main__":
    # Services
    service_prompt = ServicePrompt()
    service_files = ServiceFiles()

    service_prompt.welcome("Left Join")

    # Clean input files
    service_files.clean_excel(LEFT_JOIN, SHEET_NAME)
    service_files.clean_textfile(EXCLUSIONS)

    # Open input files
    service_files.open_file(EXCLUSIONS)
    service_files.open_file(LEFT_JOIN)

    service_prompt.wait("Please fill the input files")
    exclusion_dic_list = get_exclusion_dic()
    updated_excel_dt = remove_exclusions(exclusion_dic_list)
    service_files.write_excel(LEFT_JOIN, SHEET_NAME, updated_excel_dt)

    service_files.open_file(LEFT_JOIN)
