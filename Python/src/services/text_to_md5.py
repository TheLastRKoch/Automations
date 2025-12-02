import hashlib
from services.service_prompt import ServicePrompt
from utils import Utils
import os

FILE_PATH = r"/Users/ssegura/Documents/Workplaces/reports_toolkit/inputs/text_list.txt"
NUM_OF_URL = 15


def generate_hashes(text_list):
    hash_list_text = ""
    for text in text_list:
        hash_list_text += hashlib.md5(text.encode('utf-8')).hexdigest() + "\n"
    return hash_list_text


def clear_file():
    os.system(f"echo > {FILE_PATH}")


def open_file():
    os.popen("open "+FILE_PATH).read


if __name__ == "__main__":
    # Services
    service_prompt = ServicePrompt()

    service_prompt.welcome("Text to md5")

    # Prepare Input file
    clear_file()
    open_file()
    service_prompt.wait("Please fill")

    # Generate hashes
    text_list = Utils.get_file_items(FILE_PATH)
    hash_list_text = generate_hashes(text_list)

    # Save hashes to input file
    Utils.write_file(FILE_PATH, hash_list_text)
    open_file()
    service_prompt.message("\n\nProcess finished successfully")
