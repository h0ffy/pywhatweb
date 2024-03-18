import sys
import os
			
class Pluginpritlog_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<em id="jserror">Please enable Javascript for full functionality.</em>" },
			{ "text" : "Powered by <a href="http://pritlog.com/">Pritlog</a>" },
		]

