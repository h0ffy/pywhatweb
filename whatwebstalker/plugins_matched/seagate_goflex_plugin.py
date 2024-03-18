import sys
import os
			
class seagate_goflex_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[location]", "string" : /^https:\/\/www\.seagateshare\.com\/\?hipname=([^\s^&]+)/ }
			{ "string" : /<input id="inSubdomain" name="inSubdomain" type="text" maxlength="30" size="23" value="([^\s^"^>]*)"><br><br>/ }
	]

