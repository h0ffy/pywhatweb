import sys
import os
			
class Plugindynamicweb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="Dynamicweb ([^\s]+)"/" },
			{ "certainty" : "100", "regexp" : "/\(c\) 1999-(20[\d]{2}) Dynamicweb Software A\/S/" },
			{ "certainty" : "75", "search" : "headers[set-cookie]", "regexp" : "/Dynamicweb/" },
		]

