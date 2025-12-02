from services.service_prompt import ServicePrompt
from services.service_files import ServiceFiles
import json
import os


JSON_PATH = "/Users/ssegura/Documents/Workplaces/reports_toolkit/list.json"
CSV_PATH = "/Users/ssegura/Documents/Workplaces/reports_toolkit/list.csv"

# Setup services
file_service = ServiceFiles()
prompt_service = ServicePrompt()

# Clean input files
file_service.clean_textfile(JSON_PATH)
file_service.clean_textfile(CSV_PATH)

# Open the Json file
os.system(f"code {JSON_PATH}")
prompt_service.wait("Plase type the content of the json file")

# Convert the infomation
json_body = file_service.read_textfile(JSON_PATH)
data = json.loads((json_body))
file_service.json_csv(CSV_PATH, data)

os.system(f"open {CSV_PATH}")
