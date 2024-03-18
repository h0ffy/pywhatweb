import sys
import os
			
class Pluginjquery_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*jquery/" },
			{ "version" : "/jquery(\.min)?\.js\?ver=([0-9\.]+)['"]/", "offset" : "1 },
			{ "version" : "/jquery\/([0-9\.]+)\/jquery(\.min)?\.js/", "offset" : "0 },
			{ "version" : "/jquery-([0-9\.]+)(\.min)?\.js/", "offset" : "0 },
		]

