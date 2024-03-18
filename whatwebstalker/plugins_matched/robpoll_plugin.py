import sys
import os
			
class Pluginrobpoll_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "inurl:"robpoll.cgi?start" filetype:cgi" },
			{ "text" : "<head><title>RobPoll Admin</title></head>" },
			{ "regexp" : "/<form action="[^"]*\/robpoll\.cgi" method="post">/" },
		]
		return(self.rules)

