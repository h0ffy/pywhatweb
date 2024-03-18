import sys
import os
			
class Plugincreatelive_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/Powered by:(<a href="http:\/\/www.aspoo.cn\/" target="_blank">)?CreateLive CMS Version ([\d\.]+)/i },
			{ "version" : "/<!--By CreateLiveCms (\d)\.00-->/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/Kill=kill=(Yes|No)/" },
		]

