import sys
import os
			
class sitecaddy_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- SECTION: bottom branding -->' },
			{ "text" : '<!-- write title and meta tags -->' },
			{ "text" : '<ul class="siteCaddyMenu menuLevel0 bottomNav" id="primaryNav">' },
			{ "text" : '<a href="http://www.sitecaddy.com" title="Powered by SiteCaddy.com">' },
			{ "text" : '<img src="/mysitecaddy/assets3/common/images/poweredbysitecaddy.gif" alt="Powered by SiteCaddy.com">' },
		]

