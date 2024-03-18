import sys
import os
			
class phpfreechat_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'powered by phpfreechat"", "certainty" : '75 }
			{ "version" : '/<img src="http:\/\/www.phpfreechat.net\/pub\/logo[2]*_80x15.gif" alt="PHP FREE CHAT \[powered by phpFreeChat-([\d\.\-a-z]*)\]"/ }
		]

