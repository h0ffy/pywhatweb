import sys
import os
			
class Pluginrobpoll_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "ghdb" : "inurl:"robpoll.cgi?start" filetype:cgi" },
			{ "text" : "<head><title>RobPoll Admin</title></head>" },
			{ "regexp" : "/<form action="[^"]*\/robpoll\.cgi" method="post">/" },
		]

