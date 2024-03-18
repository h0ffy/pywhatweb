import sys
import os
			
class lasernet_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<table width="100%" height="1[\d]{2}" border="0" cellpadding="0" cellspacing="0" background="images\/headers\/[^"\/>]* ">/" },
			{ "regexp" : "/<font size="1" face="Verdana", "Arial", "Helvetica", "sans-serif">Powered by<\/font><\/font>[\s]+<a href="http:\/\/lasernet\.gr"><font size="1" face="Verdana", "Arial", "Helvetica", "sans-serif">Lasernet<\/font><\/a>[\s]+<\/td>/" },
		]

