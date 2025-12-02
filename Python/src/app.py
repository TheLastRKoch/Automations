import sys

from dotenv import load_dotenv

from services.create_ado_active_items import ServiceCreateADOActiveItems
from services.get_calendar_events import ServiceGetCalEvents
from services.clean_clipboard import ServiceCleanClipboard
from services.clone_repos import ServiceCloneRepositories
from services.check_url_list import ServiceCheckURLList
from services.schedule_job import ServiceScheduleTask
from services.open_url_list import ServiceOpenURLList
from services.get_licenses import ServiceGetLicenses
from services.generate_otp import ServiceGenerateOTP
from services.mock_api import ServiceMockAPI
from utils.prompt import UtilPrompt

# Load env variables
load_dotenv()

service_mapping = {
    "check_url_list": ServiceCheckURLList(),
    "open_url_list": ServiceOpenURLList(),
    "clone_repos": ServiceCloneRepositories(),
    "get_licenses": ServiceGetLicenses(),
    "schedule_task": ServiceScheduleTask(),
    "mock_api": ServiceMockAPI(),
    "get_calendar_events": ServiceGetCalEvents(),
    "clean_clipboard": ServiceCleanClipboard(),
    "generate_otp": ServiceGenerateOTP(),
    "create_active_ado_zenkit": ServiceCreateADOActiveItems()
}

# Service definition
prompt = UtilPrompt()

if len(sys.argv) > 1:
    sys.argv[1] in service_mapping.keys()
    if sys.argv[1] in service_mapping.keys():
        service_mapping[sys.argv[1]].run()
    else:
        prompt.message(
            "Option not found, please choose one of the next services:\n" +
            "\n".join(service_mapping.keys()))
else:
    prompt.message(
        "Option not found, please choose one of the next services:\n" +
        "\n".join(service_mapping.keys()))
