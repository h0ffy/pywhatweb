import sys
import os
			
class mkportal_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="generator" content="MKPortal" />' }
			{ "text" : '|   Cascading Style Sheet for MKportal "Forum" Portal Template' }
			{ "certainty" : '25", "text" : '<!-- end close portal body -->' }
			{ "version" : '/<a style="text-decoration: none;" href="http:\/\/www.mkportal.it\/" target="_blank">MKPortal<\/a> ([^&^<]+)(<\/b>)? &copy;2003-20[\d]{2}/ }
	]

