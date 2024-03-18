import sys
import os
			
class Pluginpragyan_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "powered by <a href="http://sourceforge.net/projects/pragyan">Pragyan CMS</a>" },
			{ "version" : "/powered by <a href="http:\/\/sourceforge.net\/projects\/pragyan" title="(Praygan|Probe) CMS">Pragyan CMS v([\d\.]+)<\/a>/", "offset" : "1 },
		]

