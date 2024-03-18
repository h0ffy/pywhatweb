import sys
import os
			
class cbs_interactive_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<script[^>]+ src="http:\/\/dw\.com\.com\/js\/dw\.js"><\/script>/ }
			{ "account" : '/<script>DW.pageParams = \{siteId:'([^']+)'\};DW.clear\(\);<\/script>/ }
			{ "account" : '/<img src="http:\/\/dw\.com\.com\/clear\/c\.gif\?sid=([^"^\s^>^&]+)/ }
	]

