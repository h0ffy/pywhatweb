import sys
import os
			
class freakauth_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<title>FreakAuth &raquo; [^<]+<\/title>/" },
			{ "regexp" : "/Welcome on board ! \/ <a href="http[^"]+">Login<\/a>		<\/div>/" },
		]

