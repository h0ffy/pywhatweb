import sys
import os
			
class vimeo_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<(param|object|embed) [^>]+vimeo\.com\/moogaloop/i },
			{ "regexp" : "/<iframe [^>]*src=['"]https?:\/\/player\.vimeo\.com\/video\//" },
		]

