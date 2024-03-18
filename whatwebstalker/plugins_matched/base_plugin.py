import sys
import os
			
class Pluginbase_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- Basic Analysis and Security Engine (BASE) -->" },
			{ "version" : "/<!-- Basic Analysis and Security Engine \(BASE\) ([\d\.]+ \([^\)]+\)) -->/" },
		]
		return(self.rules)

