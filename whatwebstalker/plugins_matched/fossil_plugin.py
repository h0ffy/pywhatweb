import sys
import os
			
class fossil_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<div class="footer">\s+(<a href="http:\/\/fossil-scm\.org">Fossil<\/a>|Fossil) version \[([^\]]+)\] [\d]{4}\-[\d]{2}\-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}/", "offset" : "1 },
			{ "string" : /<div class="footer">\s+(<a href="http:\/\/fossil-scm\.org">Fossil<\/a>|Fossil) version \[[^\]]+\] ([\d]{4}\-[\d]{2}\-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2})/", "offset" : "1 },
		]

