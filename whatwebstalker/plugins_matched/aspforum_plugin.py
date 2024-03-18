import sys
import os
			
class aspforum_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<div[^>]+id="FORUMS_FORUM_GROUP_V([\d_]+)/", "name" : 'version" }
	]

