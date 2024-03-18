import sys
import os
			
class inktomi_search_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "version" : '/^Inktomi Search ([^\s]+)$/ }
			{ "url" : '/util/badkey.html", "version" : '/<font size="\+1"><b>License Key Problems<\/b><\/font><br>[\s]+<b>Inktomi Search ([^<^\s]+)<\/b><br>/ }
	]

