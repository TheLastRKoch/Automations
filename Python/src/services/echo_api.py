from flask import Flask, request
from services.service_files import ServiceFiles
import json

from services.service_prompt import ServicePrompt

FILE_PATH = "/Users/ssegura/Documents/Workplaces/reports_toolkit/echo_api"
PORT = "5000"

app = Flask(__name__)


@app.route("/json", methods=["POST"])
def base():
    service_file = ServiceFiles()
    service_file.write_textfile(
        f"{FILE_PATH}/echo.json", json.dumps(request.get_json())
    )
    print(base.__name__ + " saved")
    return {}


@app.route("/xlsx", methods=["POST"])
def xlsx():
    service_file = ServiceFiles()
    service_file.write_textfile(f"{FILE_PATH}/echo.xlsx", request.get_json())
    print(xlsx.__name__ + " saved")
    return {}


if __name__ == "__main__":
    app.run(debug=True)

    service_prompt = ServicePrompt()
    service_prompt.clear()
    service_prompt.message(f"Echo API https://localhost:{PORT}")
