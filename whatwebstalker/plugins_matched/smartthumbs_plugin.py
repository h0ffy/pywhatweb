import sys
import os
			
class smartthumbs_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/POWERED[\s]+BY[\s]+<a href="http:\/\/www.smart-scripts.com">SMART THUMBS<\/a>/ },
			{ "text" : 'POWERED BY<span> <a href="http://www.thumbsrotator.com"><b><span style="font-size: 11px; font-family: Verdana", "Arial;">SMART THUMBS</span>' },
		]

