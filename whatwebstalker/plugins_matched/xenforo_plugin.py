import sys
import os
			
class Pluginxenforo_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "name" : "HTML id element", ":"regex" : "/<html[^>]+id="XenForo"},
			{ "search" : "headers[set-cookie]", "regexp" : "/^xf_session/", "name" : "xf_session cookie" },
		]

