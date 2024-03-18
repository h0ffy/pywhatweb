import sys
import os
			
class rips_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<div class="logo"><a id="logo" href="http:\/\/sourceforge\.net\/projects\/rips-scanner\/files\/" target="_blank" title="get latest version">([^<^\s]+)<\/a><\/div>/ }
			{ "text" : '<td nowrap><input type="checkbox" id="subdirs" value="1" title="check to scan subdirectories" />subdirs</td>' }
		]

