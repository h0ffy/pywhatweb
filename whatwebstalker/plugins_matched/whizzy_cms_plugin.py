import sys
import os
			
class Pluginwhizzy_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/Powered by Whizzy CMS <big>&spades;<\/big> <\/a><\/div><!-- \[Whizzy CMS:Whizzy CMS ([^\]]+)/" },
		]

