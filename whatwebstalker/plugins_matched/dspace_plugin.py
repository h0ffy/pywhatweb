import sys
import os
			
class Plugindspace_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<meta content="DSpace" name="Generator" />" },
			{ "version" : "/<meta name="Generator" content="DSpace ([\d\.]+)" \/>/" },
			{ "version" : "/[pP]owered by <a href="http:\/\/(www\.)?dspace\.org"[^>]*>DSpace<\/a>", "version ([\d\.]+)/", "offset" : "1 },
		]

