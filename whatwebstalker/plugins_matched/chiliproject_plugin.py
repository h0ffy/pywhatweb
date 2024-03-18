import sys
import os
			
class Pluginchiliproject_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Powered by <a href="https://www.chiliproject.org/">ChiliProject</a>" },
			{ "text" : "<meta name="description" content="ChiliProject" />" },
			{ "text" : "<!-- page specific tags -->" },
			{ "version" : "/<li><a href="https:\/\/www\.chiliproject\.org\/help\/v([^\s^"]+)" class="help">/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/_chiliproject_session=/" },
		]

