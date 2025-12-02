from os import environ as env
from flask import Flask
import jmespath
import json

from utils.file import UtilFile
from utils.prompt import UtilPrompt


class ServiceMockAPI:
    def handler(self, response: dict, status_code):
        return response, status_code

    def run(self):

        # Utils definition
        util_file = UtilFile()
        prompt = UtilPrompt()

        route_list_path = env["ROUTE_LIST_PATH"]
        util_file.open(route_list_path)
        prompt.wait("Please configure the endpoints then press any key")
        route_list = json.loads(util_file.read_text_file(route_list_path))

        if route_list is None or len(route_list) > 0:
            app = Flask(__name__)

            query = jmespath.compile(r"[].path")
            path_list = query.search(route_list)

            app.add_url_rule(rule="/",
                             view_func=lambda response=path_list, status_code=200: self.handler(
                                 response, status_code),
                             endpoint="Index")

            for route in route_list:
                name = route.get("name")
                path = route.get("path")
                allowed_methods = route.get("allowed_methods")
                response = route.get("response")
                status_code = route.get("status_code")

                app.add_url_rule(rule=path,
                                 view_func=lambda response=response, status_code=status_code: self.handler(
                                     response, status_code),
                                 endpoint=name,
                                 methods=allowed_methods)
            app.run(debug=True)
            print("Mock API running")
        else:
            print("Error: Could not load the configured endpoints.")
