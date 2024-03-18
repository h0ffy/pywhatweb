import sys
import os
			
class wp_slimstat_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[set-cookie]", "regexp" : '/slimstat_tracking_code=[a-f\d]{32};/ },
		]

