import sys
import os
			
class Pluginfree_realty_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<!--FreeRealty ([^\s]+) -->/" },
			{ "text" : "<font class="foot">This tool is Open Source and released under the <a href="http://www.gnu.org/copyleft/gpl.html">GPL</a></font>" },
			{ "text" : "<!-- THUS ENDETH THE MAIN CONTENT -->" },
			{ "text" : "<!-- HERE BEGINNETH THE FOOTER --><div class="foot">" },
		]

