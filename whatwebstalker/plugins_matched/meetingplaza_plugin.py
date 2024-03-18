import sys
import os
			
class Pluginmeetingplaza_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "text" : "<html> <body> Hello. I\'m MeetingPlaza HTTP Tunneling Server.<br>Date: " },
			{ "version" : "/^InterSpace HTTP Tunneling\/([^\s]+)$/", "search" : "headers[server]" },
			{ "regexp" : "/^InterSpace HTTP Tunneling/", "search" : "headers[server]" },
		]
		return(self.rules)

