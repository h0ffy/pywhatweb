import sys
import os
			
class Pluginhyperic_hq_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "url" : "/ui_docs/DOC/index.html", "version" : "/<title>DOCS\d+ \(vFabric Hyperic ([^\)]+)\)/" },
			{ "text" : "<a id="screencastLink" href="http://www.hyperic.com/demo/screencasts.html" target="_blank" title="Screencasts">" },
			{ "search" : "headers[location]", "regexp" : "/\/app\/login;jsessionid=/" },
		]

