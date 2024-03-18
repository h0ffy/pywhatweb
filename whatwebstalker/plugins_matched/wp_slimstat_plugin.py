import sys
import os
			
class Pluginwp_slimstat_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[set-cookie]", "regexp" : "/slimstat_tracking_code=[a-f\d]{32};/" },
		]
		return(self.rules)

