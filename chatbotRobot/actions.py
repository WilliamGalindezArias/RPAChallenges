import configparser
from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

config = configparser.ConfigParser()
config.read_file(open("bot.cfg"))

TOKEN = config.get('UIPATH', 'ACCESS_TOKEN')
URL = config.get('UIPATH', 'URL')


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_robot_message"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("I am calling my Friend Robot")
        message_to_rpa = tracker.get_slot('message')

        header = {'Authorization': 'Bearer' + TOKEN,
                  'X-UIPATH-TenantName': "WilliamDefa0scq105711",
                  'Content-Type': 'application/json'}
        message = {"message": f'"{message_to_rpa}"'}
        body = {"startInfo":
                    {"ReleaseKey": "b145a984-903f-49c5-bedc-b03b5145876c",
                     "Strategy": "Specific",
                     "RobotIds": [202770],
                     "JobsCount": 0,
                     "Source": "Manual",
                     # "InputArguments": "{ \" message\" : " + "'" + message_to_rpa + "'" + "}"
                     # "InputArguments": "{ \" message\" : " + f'" {message_to_rpa}"' + "}"
                     "InputArguments": str(message)

                     }}
        print(body)
        url = "https://platform.uipath.com/willibjekpmu/WilliamDefa0scq105711"
        api = "/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs"
        response = requests.post(url + api, json=body, headers=header)
        print(url + api)
        print('\n', response)

        return []
