import sys
import os
			
class Pluginnetwork_tracker_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<p><small>powered by <a href="http://networktracker.org" target="_blank" title="network tracker website">network tracker</a></small></p>" },
		]
		return(self.rules)

