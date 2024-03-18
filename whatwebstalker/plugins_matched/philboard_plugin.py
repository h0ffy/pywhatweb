import sys
import os
			
class philboard_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : "powered by philboard" inurl:philboard.asp", "certainty" : "75 },
			{ "version" : "/<img src="images\/philboard_small.gif" alt="powered by philboard [v]*([\d\.]+)" width="76" height="21" border="0" align="middle">/" },
		]

