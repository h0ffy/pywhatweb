import sys
import os
			
class Pluginesitesbuilder_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- created by XTLabs", "Inc. http://www.xt-labs.com -->" },
			{ "regexp" : "/<a [^href]+href="http:\/\/[www\.]*esitesbuilder.com">Powered by eSitesBuilder<\/a>/" },
			{ "text" : "Powered by <a href="http://www.esitesbuilder.com/" target="_blank" alt="website builder">eSitesBuilder</a>" },
			{ "text" : "All rights reserved. Powered by eSitesBuilder" },
			{ "regexp" : "/Powered by[&nbsp;]*[\s]*<a [^href]+href="http:\/\/[www\.]*esitesbuilder.com">eSitesBuilder<\/a>/" },
			{ "text" : "Powered by <a href="http://www.esitesbuilder.com/" target="_blank" alt="website builder">eSitesBuilder</a>" },
		]
		return(self.rules)

