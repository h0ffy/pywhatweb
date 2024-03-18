import sys
import os
			
class Pluginxenforo_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "HTML id element", ":"regex" : "/<html[^>]+id="XenForo"},
			{ "search" : "headers[set-cookie]", "regexp" : "/^xf_session/", "name" : "xf_session cookie" },
		]
		return(self.rules)

