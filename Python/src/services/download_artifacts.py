from services.service_command import ServiceCommand
from services.service_prompt import ServicePrompt
from services.service_files import ServiceFiles
import json
import os
import re

ARTIFACT_LIST_PATH = "/Users/ssegura/Documents/Workplaces/reports_toolkit/inputs/artifact_list.txt"
OUTPUT_PATH = "/Users/ssegura/Documents/Workplaces/reports_toolkit/artifacts"
PULL_CONTAINER_CMD = "podman pull {container_image}"
SAVE_CONTAINER_CMD = 'podman export $(podman create --name {container_name} {container_image} ) --output="{output_path}"'
DELETE_CONTAINER_CMD = 'podman rm {container_name}'
DELETE_CONTAINER_IMAGE_CMD = 'podman image rm {container_image}'
ARTIFACT_NAME_PATTERN = r".+?\/"
TEMP_CONTAINER_NAME = "temp-container"


def create_org_folder(org_name):
    path = OUTPUT_PATH+"/"+org_name
    if not os.path.exists(path):
        os.makedirs(path)


def format_artifact_name(artifact_name):
    artifact_name.replace("_", "-")
    return re.sub(ARTIFACT_NAME_PATTERN, "", artifact_name)


def pull_container_image(url):
    service_cmd = ServiceCommand()
    service_cmd.script(PULL_CONTAINER_CMD.format(container_image=url))


def saving_container_image(url, org_name, image_name):
    service_cmd = ServiceCommand()
    service_cmd.script(SAVE_CONTAINER_CMD.format(
        container_image=url,
        container_name=f"{TEMP_CONTAINER_NAME}-{org_name}",
        output_path=f"{OUTPUT_PATH}/{org_name}/{image_name}.zip"
    ))


def delete_container(org_name):
    service_cmd = ServiceCommand()
    service_cmd.script(DELETE_CONTAINER_CMD.format(
        container_name=f"{TEMP_CONTAINER_NAME}-{org_name}"
    ))


def delete_container_image(url):
    service_cmd = ServiceCommand()
    service_cmd.script(DELETE_CONTAINER_IMAGE_CMD.format(
        container_image=url,
    ))


if __name__ == "__main__":
    # Services
    service_files = ServiceFiles()
    service_prompt = ServicePrompt()

    # Get the input information
    service_files.clean_textfile(ARTIFACT_LIST_PATH)
    service_files.open_file(ARTIFACT_LIST_PATH)
    service_prompt.wait("Please fill the input file")

    # Read the input file
    artifact_list = json.loads(service_files.read_textfile(ARTIFACT_LIST_PATH))
    org_name = service_prompt.question("Please type the organization name")
    create_org_folder(org_name)

    # service_prompt.message(f"Found {len(artifact_list)} images")
    # service_prompt.message("Start processing")

    for artifact in artifact_list:
        artifact_name = format_artifact_name(artifact)
        artifact_url = artifact_list[artifact]
        pull_container_image(artifact_url)
        saving_container_image(artifact_url, org_name, artifact_name)
        delete_container(org_name)
        delete_container_image(artifact_url)
