import sys
import os
			
class alcatel_lucent_omniswitch_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>Webview Logon Page</title>' }
			{ "text" : 'document.write(errMsg=="?"&nbsp;":("<u>Error</u>&nbsp;-&nbsp;" + errMsg));' }
	]

