import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class OrchestratorAPI(object):
    
    def parameters(self):
        access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlJUTkVOMEl5T1RWQk1UZEVRVEEzUlRZNE16UkJPVU00UVRRM016TXlSalUzUmpnMk4wSTBPQSJ9.eyJodHRwczovL3VpcGF0aC9lbWFpbCI6IndpbGxpYW0uZ3B1Mi5lbnZAZ21haWwuY29tIiwiaHR0cHM6Ly91aXBhdGgvZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vYWNjb3VudC51aXBhdGguY29tLyIsInN1YiI6ImF1dGgwfDVkMzg0NTgzNGFkNTEyMGRkZmUxMzU1MCIsImF1ZCI6WyJodHRwczovL29yY2hlc3RyYXRvci5jbG91ZC51aXBhdGguY29tIiwiaHR0cHM6Ly91aXBhdGguZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU2NDQwNzQ5MCwiZXhwIjoxNTY0NDkzODkwLCJhenAiOiI1djdQbVBKTDZGT0d1NlJCOEkxWTRhZExCaEl3b3ZRTiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MifQ.sEYiFqj2RyKKZLlwee1mvmUwF4LT5T3cLICyh8zTkNFsjxky2uwCPIbcZe3TT5Y0Qvt1M6hPycnEOYordy6PdnNhF_NJN_bPwOLTfQmiC4ufR03K6A_FGinKSn5-j6NpPy8MxL89jtMjx9NgSnpijiMrpzLhRKXkJ0J6LNGvhMFuyf5eUWq09yCeH6-q-k8KU4eO9jCnSdlbS-8KH_Jsr4FVHI5MWmQ9_b3JYZHs_WAkRAAfGdzAPgk6-vdomKllJReGeDjtjk022jqp4hkuhHAMjPq06LDyQVMJkG_7Yr12q9fwfPhUJxV_twKD-XJY4-DkKYReEHYgo8xneQ_Vrg"
        header = {'Authorization': 'Bearer' + access_token,
                 'X-UIPATH-TenantName': "WilliamDefa0scq105711",
                 'Content-Type': 'application/json'}
        body = { "startInfo":
               { "ReleaseKey": "b145a984-903f-49c5-bedc-b03b5145876c",
                "Strategy": "Specific",
                 "RobotIds": [ 202770 ],
                 "JobsCount": 0,
                 "Source": "Manual",
             "InputArguments":"{\"message\":\"From Bot ?\"}"
 
               } }
        url = "https://platform.uipath.com/willibjekpmu/WilliamDefa0scq105711"
        api = "/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs"
        response = requests.post(url+api, json=body, headers = header)
        print(url+api)
        return response

class RobotMessage(Action):
    def name(self):
        return "action_robot_message"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("calling the robot")
        access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlJUTkVOMEl5T1RWQk1UZEVRVEEzUlRZNE16UkJPVU00UVRRM016TXlSalUzUmpnMk4wSTBPQSJ9.eyJodHRwczovL3VpcGF0aC9lbWFpbCI6IndpbGxpYW0uZ3B1Mi5lbnZAZ21haWwuY29tIiwiaHR0cHM6Ly91aXBhdGgvZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vYWNjb3VudC51aXBhdGguY29tLyIsInN1YiI6ImF1dGgwfDVkMzg0NTgzNGFkNTEyMGRkZmUxMzU1MCIsImF1ZCI6WyJodHRwczovL29yY2hlc3RyYXRvci5jbG91ZC51aXBhdGguY29tIiwiaHR0cHM6Ly91aXBhdGguZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU2NDQwNzQ5MCwiZXhwIjoxNTY0NDkzODkwLCJhenAiOiI1djdQbVBKTDZGT0d1NlJCOEkxWTRhZExCaEl3b3ZRTiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MifQ.sEYiFqj2RyKKZLlwee1mvmUwF4LT5T3cLICyh8zTkNFsjxky2uwCPIbcZe3TT5Y0Qvt1M6hPycnEOYordy6PdnNhF_NJN_bPwOLTfQmiC4ufR03K6A_FGinKSn5-j6NpPy8MxL89jtMjx9NgSnpijiMrpzLhRKXkJ0J6LNGvhMFuyf5eUWq09yCeH6-q-k8KU4eO9jCnSdlbS-8KH_Jsr4FVHI5MWmQ9_b3JYZHs_WAkRAAfGdzAPgk6-vdomKllJReGeDjtjk022jqp4hkuhHAMjPq06LDyQVMJkG_7Yr12q9fwfPhUJxV_twKD-XJY4-DkKYReEHYgo8xneQ_Vrg"
        header = {'Authorization': 'Bearer' + access_token,
                 'X-UIPATH-TenantName': "WilliamDefa0scq105711",
                 'Content-Type': 'application/json'}
        body = { "startInfo":
               { "ReleaseKey": "b145a984-903f-49c5-bedc-b03b5145876c",
                "Strategy": "Specific",
                 "RobotIds": [ 202770 ],
                 "JobsCount": 0,
                 "Source": "Manual",
             "InputArguments":"{\"message\":\"From Bot ?\"}"
 
               } }
        url = "https://platform.uipath.com/willibjekpmu/WilliamDefa0scq105711"
        api = "/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs"
        response = requests.post(url+api, json=body, headers = header)
        print(url+api)
        return response
        #robot_api = 





# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []
