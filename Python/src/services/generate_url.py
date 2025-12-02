from services.service_files import ServiceFiles
from services.service_prompt import ServicePrompt

URL_FINAL_PATH = "/Users/ssegura/Desktop"
URL_TEMPLATE_PATH = "Resources/URL_Template.url"

if __name__ == "__main__":
    # Services
    file_service = ServiceFiles()
    prompt_service = ServicePrompt()

    prompt_service.welcome("Generate Custom URL File")

    url_template = file_service.read_textfile(URL_TEMPLATE_PATH)

    file_name = prompt_service.question("Please type the name of the file")
    url = prompt_service.question("Please type the URL")

    url_template = url_template.format(
        url=url
    )
    url_path = f"{URL_FINAL_PATH}/{file_name}.url"
    file_service.write_textfile(url_path, url_template)
