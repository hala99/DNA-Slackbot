import json
import logging
import os
import requests
import threading
import config_hb
from flask import Flask, jsonify, config, request, session, make_response, Response
from slackclient import SlackClient
from snapshots import SnapshotManager
# A Slack client and webserver 
# Your app's Slack bot user token
SLACK_BOT_TOKEN = os.environ["xoxp-296834659428-296910710660-299555639330-ec4c73b8d028b940d0825f65a00493bf"]

# Slack client for Web API requests
slack_client = SlackClient(config_hb.SLACK_TOKEN, None)

# Flask webserver for incoming traffic from Slack
app = Flask(__name__)
app.url_map.strict_slashes = False
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#options for the scroll down menu
@app.route("/slack/message_options", methods=["POST"])
def message_options():
    # Parse the request payload
    form_json = json.loads(request.form["payload"])
    {
    "text": "What would you like to do?",
    "response_type": "in_channel",
    "attachments": [
        {
            "text": "Choose an option: ",
            "fallback": "If you could read this message, you'd be choosing something fun to do right now.",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "callback_id": "option_selection",
            "actions": [
                {
                    "name": "options_list",
                    "text": "Pick an option...",
                    "type": "select",
                    "options": [
                        {
                            "text": "dnasnapshots",
                            "value": "snapshots"
                        },
                        {
                            "text": "dnastreams",
                            "value": "streams"
                        },
                        {
                            "text": "dnahelp",
                            "value": "help"
                        },
                        {
                            "text": "dnalogout",
                            "value": "logout"
                        }
                        return Response(json.dumps(options_list), mimetype='application/json')
                    ]
                }
            ]
        }
    ]
}


#the interaction of the user
@app.route("/slack/message_actions", methods=["POST"])
def message_actions():
# Parse the request payload
    form_json = json.loads(request.form["payload"])

    # Check to see what the user's selection was and update the message
    user_selection = form_json["actions"][0]["selected_options"][0]["value"]
    user = SnapshotManager(user_key, api_domain)
    if user_selection == "help":
        return help_command(user)
    elif user_selection == "snapshots":
        return user.list_snapshots(user)
    elif user_selection == "logout":
        return logout(user)


{
    "actions": [
        {
            "name": "options_list",
            "selected_options": [
                {
                    "value": "help"
                }
            ]
        }
    ],
    "callback_id": "option_selection",
    "team": {
        "id": "T8QQJKDCL",
        "domain": "pocket-calculator"
    },
    "channel": {
        "id": "C8QQXAQ4S",
        "name": "general"
    },
    "user": {
        "id": "U8QSSLWKE",
        "name": "ruchi"
    },
    "action_ts": "1481579588.685999",
    "message_ts": "1481579582.000003",
    "attachment_id": "1",
    "token": "verification_token_string",
    "original_message": {
        "text": "pick an option..",
        "bot_id": "B08BCU62D",
        "attachments": [
            {
                "callback_id": "option_selection",
                "fallback": "Upgrade your Slack client to use messages like these.",
                "id": 1,
                "color": "3AA3E3",
                "actions": [
                    {
    
                        "name": "options_list",
                        "text": "Pick an option...",
                        "type": "select",
                        "options": [
                            {
                                "text": "dnasnapshots",
                                "value": "snapshots"
                            },
                            {
                                "text": "dnastreams",
                                "value": "streams"
                            },
                            {
                                "text": "dnalogout",
                                "value": "logout"
                            }
                        ]
                    }
                ]
            }
        ],
        "type": "message",
        "subtype": "bot_message",
        "ts": "1481579582.000003"
    },
    #this a webhook url from slack 
    "response_url": "https://hooks.slack.com/services/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",
    "trigger_id": "13345224609.738474920.8088930838d88f008e0"
}
   
#we are not sure if this part should be here!:)
@app.route('/dnalogout', methods=['GET','POST'])
def logout():
    session['logged_in'] = False
    return "Sucessfully logged out"

@app.route('/dnahelp',methods=['GET','POST'])
def help_command(user_key):
	#print request.form
	return """ Need some help? Take a look at the /DNA slash commands and their descriptions below: 
			\n1. /DNALogin: Use this slash command to login to see the status of your snapshot.
			\n2. /DNALogout: Use this slash command to logout of the DNA slack app. 
			\n3. /DNASnapshot: Use this slash command to 
			\n4. /DNAStreams: 
			"""

