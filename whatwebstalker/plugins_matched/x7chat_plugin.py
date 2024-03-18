import sys
import os
			
class x7chat_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : "75", "ghdb" : "inurl:x7chat "Please enter your username and password to login"" },
			{ "version" : "/Powered By <a href="http:\/\/www.x7chat.com\/" target="_blank">X7 Chat<\/a> ([\d\.A-Z]+)[\s]*[^&]*&copy; 2004 By The <a href="http:\/\/www.x7chat.com\/" target="_blank">X7 Group<\/a>/" },
			{ "version" : "/<Br><font size="2">Powered By X7 Chat Version ([^<]+)<\/font>/" },
		]

