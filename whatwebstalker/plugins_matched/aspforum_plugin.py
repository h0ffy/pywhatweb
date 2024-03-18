import sys
import os
			
class Pluginaspforum_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div[^>]+id="FORUMS_FORUM_GROUP_V([\d_]+)/", "name" : "version" },
		]
		return(self.rules)

