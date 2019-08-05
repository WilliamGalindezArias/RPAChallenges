## happy path: Invoices               <!-- name of the story - just for debugging -->
* greeting              
  - utter_greet
* triggerRPA       
  - action_robot_message
* bye
  - utter_goodbye
  - action_restart
  
## happy path: Invoices               <!-- name of the story - just for debugging -->
* greeting              
  - utter_greet
* triggerRPA{"message" : "invoices"}       
  - action_robot_message
* bye
  - utter_goodbye
  - action_restart
  
  
## happy path: open app               <!-- name of the story - just for debugging -->
* greeting              
  - utter_greet
* triggerRPA{"message" : "notepad"} 
  - action_robot_message
* bye
  - utter_goodbye
  - action_restart
  
## Did that help
* greeting              
  - utter_greet
* triggerRPA{"message" : "chatbot says hi"} 
  - action_robot_message
  - utter_did_that_help
* bye
  - utter_goodbye
  - action_restart
  