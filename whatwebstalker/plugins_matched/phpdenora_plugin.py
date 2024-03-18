import sys
import os
			
class Pluginphpdenora_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "25", "ghdb" : "powered by phpDenora" intitle:"phpDenora"" },
			{ "string" : /<meta name="Description" content="IRC Statistics for (.+) powered by phpDenora" \/>/" },
			{ "version" : "/<td><h6 class="right">Powered by <a href="http:\/\/(phpdenora.pimpmylinux.org|denorastats.org)\/">phpDenora<\/a> v([^<]+)<\/h6><\/td>/", "offset" : "1 },
		]

