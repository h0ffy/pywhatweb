import sys
import os
			
class help_desk_software_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<div class="AdminTDSmall">[\s]+powered by <a href="http:\/\/freehelpdesk\.org\/\?ver=([^"^>^\s]+)" target="_blank">freehelpdesk\.org<\/a>[\s]+<\/div>/ }
			{ "version" : '/<\/html>[\s]+<font style='font-size:0px'>([^<^\s]+)<\/font>/ }
		]

