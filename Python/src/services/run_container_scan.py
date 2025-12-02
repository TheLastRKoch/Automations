from utils import Utils
import os
import re

# Constants
IMAGES_PATH = r"/Users/ssegura/Documents/Workplaces/reports_toolkit/inputs/images.txt"
REPORT_PATH = r"/Users/ssegura/Documents/Workplaces/grype/Reports"


def menu_start():
    os.system("clear")
    print("The container scannig process just started")


def menu_repository_info(repository):
    print(f"\n\n\nProcessing {repository}...\n")


def menu_stop(repository_number):
    print(
        f"\n\nThe process has finished successfully scanned {repository_number} repositories")


def get_image_repository(image):
    return image.split("/")[-1]


def run_container_scan(image):
    return os.popen(f"grype {image}  --scope all-layers --add-cpes-if-none").read()


def format_report(text_output):
    return re.sub(r" {2,}", ",", text_output)


def generate_report(formated_text, repository):
    report_body = r"sep=,"+"\n"+formated_text
    path = f"{REPORT_PATH}/{repository}.csv"
    Utils.write_file(path, report_body)


if __name__ == "__main__":
    menu_start()
    image_list = Utils.get_file_items(IMAGES_PATH)

    for image in image_list:
        repository = get_image_repository(image)
        menu_repository_info(repository)
        text_output = run_container_scan(image)
        formated_text = format_report(text_output)
        generate_report(formated_text, repository)

    menu_stop(len(image_list))
