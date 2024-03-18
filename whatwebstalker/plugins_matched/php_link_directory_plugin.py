import sys
import os
			
class php_link_directory_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'powered by phpLinkDirectory"", "certainty" : '25 },
			{ "regexp" : '/<a href="http:\/\/www.phplinkdirectory.com[^>]*Phplinkdirectory/i },
			{ "version" : '/<meta name="generator"[^>]*content="PHP Link Directory ([0-9\.]+)"/ },
		]

