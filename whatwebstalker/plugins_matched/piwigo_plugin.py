import sys
import os
			
class piwigo_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="generator" content="Piwigo (aka PWG)", "see piwigo.org">' }
			{ "text" : '<meta name="generator" content="Piwigo", "piwigo.org">' }
			{ "regexp" : '/<div id="copyright">\s+<a name="EoP"><\/a>\s+<!-- End of Page -->/ }
			{ "regexp" : '/Powered by\s+<a href="http:\/\/piwigo\.org" class="Piwigo">/ }
		]

