import sys
import os
			
class Pluginjquery_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*jquery/" },
			{ "version" : "/jquery(\.min)?\.js\?ver=([0-9\.]+)['"]/", "offset" : "1 },
			{ "version" : "/jquery\/([0-9\.]+)\/jquery(\.min)?\.js/", "offset" : "0 },
			{ "version" : "/jquery-([0-9\.]+)(\.min)?\.js/", "offset" : "0 },
		]
		return(self.rules)

