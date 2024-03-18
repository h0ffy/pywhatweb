import sys
import os
			
class Pluginweb_calendar_system_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "25", "ghdb" : "+intitle:"Web Calendar system v" inurl:.asp" },
			{ "version" : "/<TITLE>Web Calendar system v ([\.\d]+)<\/TITLE>/" },
		]

