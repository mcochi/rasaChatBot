from rasa_sdk import ActionExecutionRejection
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT, Action
from rasa.core.slots import Slot
from typing import Dict, Text, Any, List, Union
import requests
URL = "http://83.32.158.101:3002/lora_gps_last"

class SalesForm(FormAction):
    """Collects sales Information and adds it to the spreadsheet"""


    @staticmethod
    def required_slots(trackeer):
        return [
            "job_function",
            "use_case",
            "budget",
            "person_name",
            "company",
            "business_email"
        ]

    def submit(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],
    ) -> List[Dict]: 
        res = requests.get(url=URL)
        res.json
        dispatcher.utter_message(res.text) 
        return []


    def name(self):
        return "sales_form"
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        return {"use_case": self.from_text(intent="inform"), "company": self.from_text(intent="inform")}