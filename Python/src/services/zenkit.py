from utils.jmespath import UtilsJMESpath
from os import environ as env
import requests


class ServiceZenkit:

    def __init__(self, api_token):

        # Define services
        self.jmespath = UtilsJMESpath()

        self.headers = {
            "Zenkit-API-Key": api_token,
            "Content-Type": "application/json",
        }
        self.base_url = env["ZENKIT_BASE_URL"]

        self.items_per_page = int(env["ZENKIT_ITEMS_PER_PAGE"])

    def check_token_auth(self):
        url = self.base_url + "/users/me"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return True
        return False

    def create_task(self, list_id, title):
        url = self.base_url + f"/lists/{list_id}/entries"
        payload = {"5a575b77-178c-4da6-9a0b-52a8bb2dccf0_text": title}
        return requests.post(url, headers=self.headers, json=payload)

    def get_list_element(self, list_id):
        url = self.base_url + f"/lists/{list_id}/elements"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()

        return response.json()

    def get_list_columns(self, list_id):
        url = self.base_url + f"/lists/{list_id}/elements"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()

        columns_dic = {}

        for item in response.json():
            resource_role = item.get("resourceRole")
            element_id = item.get("id")
            uuid = item.get("uuid")

            columns_dic.update({
                f"{resource_role}_{record}": {
                    "id": element_id,
                    "column_name": f"{uuid}_{record}",
                }
                for record in item.get("businessData", [])
            })
        return columns_dic
