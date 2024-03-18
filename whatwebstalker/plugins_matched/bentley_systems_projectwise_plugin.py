import sys
import os
			
class bentley_systems_projectwise_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '</title><meta http-equiv="X-UA-Compatible" content="IE=8" /><link rel="shortcut icon" href="ProjectWise.ico" />' }
			{ "regexp" : '/<title>\s+ProjectWise Web Server\s+<\/title>/ }
			{ "certainty" : '75", "text" : '<!-- Initially invisible login form -->' }
			{ "search" : 'headers[set-cookie]", "regexp" : '/Bentley.WebSession=/ }
			{ "url" : '/ProjectWise.ico", "md5" : 'c20606b0a22e4c91940798a485d7eff7" }
	]

