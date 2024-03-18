import sys
import os
			
class support_incident_tracker_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<div id='masthead'><h1 id='apptitle'><span>SiT! Support Incident Tracker</span></h1></div>" },
			{ "version" : '/<meta name="GENERATOR" content="SiT! Support Incident Tracker v([^"]+)" \/>/ },
			{ "text" : '<div class='windowtitle'>SiT! - Login</div>" },
		]

