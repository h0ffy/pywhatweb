import sys
import os
			
class jcore_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<script type='text\/javascript'>\s+var JCORE_VERSION = '([^']+)';/" },
			{ "version" : "/<link href='https?:\/\/[^'^\?]+\/static\.php\?request=css(&amp;admin=1)?&amp;[\d]+\-v([\d\.]+)/", "offset" : "1 },
		]

