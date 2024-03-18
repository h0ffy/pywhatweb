import sys
import os
			
class Pluginsitegenius_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "inurl:"sitegenius/topic.php"" },
			{ "regexp" : "/var PortalBrowser = window.open\('popup.php\?page_type='\+page_type\+'&lang=[A-Z]{2}&page_id='\+pgid(\+addToURL)?", "'", "myFeatures\); /" },
		]

