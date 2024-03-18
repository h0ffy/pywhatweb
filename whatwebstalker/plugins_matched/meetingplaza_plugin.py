import sys
import os
			
class meetingplaza_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : "25", "text" : "<html> <body> Hello. I\'m MeetingPlaza HTTP Tunneling Server.<br>Date: " },
			{ "version" : "/^InterSpace HTTP Tunneling\/([^\s]+)$/", "search" : "headers[server]" },
			{ "regexp" : "/^InterSpace HTTP Tunneling/", "search" : "headers[server]" },
		]

