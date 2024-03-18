import sys
import os
			
class pear_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "string" : /<h2><a id="top0">([\d]+ Installed Packages)", "Channel / },
			{ "module" : /<h2><a id="pkg_([^\s^\"]+)"><\/a><a/ },
			{ "certainty" : '75", "text" : '<title>PEAR :: PEAR_Info()</title>' },
			{ "filepath" : '/<tr class="v">\s+<td class="e">www_dir<\/td>\s+<td>([^<]+)<\/td>\s+<\/tr>/ },
		]

