import sys
import os
			
class whiteboard_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '			&copy; <a href="http://www.powerwd.com">SaroSoftware</a><br />", "certainty" : '75 },
			{ "version" : '/Powered By WhiteBoard ([\d\.]+)<br \/>/ },
			{ "version" : '/Powered By WhiteBoard <span id="version">([\d\.]+)<\/span><br \/>/ },
		]

