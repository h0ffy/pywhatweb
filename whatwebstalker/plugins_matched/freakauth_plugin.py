import sys
import os
			
class Pluginfreakauth_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<title>FreakAuth &raquo; [^<]+<\/title>/" },
			{ "regexp" : "/Welcome on board ! \/ <a href="http[^"]+">Login<\/a>		<\/div>/" },
		]
		return(self.rules)

