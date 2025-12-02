import json

from os import environ as env

from utils.webrequest import UtilWebRequest
from services.zenkit import ServiceZenkit


class ServiceCreateADOActiveItems:

    def __init__(self):
        self.webrequest = UtilWebRequest()

    def generate_headers(self):
        return {
            'Authorization': f'Bearer {env["ADO_TOKEN"]}',
        }

    def get_work_items_from_query(self, query_url):
        return self.webrequest.get(url=query_url,
                                   headers=self.generate_headers())

    def get_work_item_details(self, url_list, work_item_id):
        return self.webrequest.get(
            url=url_list["Get Workitem"].format(work_item_id=work_item_id),
            headers=self.generate_headers())

    def run(self):
        url_list = json.loads(env["ADO_URL_LIST"])
        zenkit = ServiceZenkit(api_token=env["ZENKIT_TOKEN"])
        created_counter = 0

        work_item_list = self.get_work_items_from_query(
            url_list["Actively working on"])
        for work_item_row in work_item_list.get("workItems", {}):
            if work_item_id := work_item_row.get("id"):
                work_item = self.get_work_item_details(
                    url_list=url_list, work_item_id=work_item_id)
                title = work_item.get("fields", {}).get("System.Title")
                if title:
                    zenkit.create_task(list_id="3761914", title=title)
                    created_counter = created_counter + 1
        print(
            f'From {len(work_item_list.get("workItems", {}))} work items identified in ADO, {created_counter} were created in Zenkit.'
        )
