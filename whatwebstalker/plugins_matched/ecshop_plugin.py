import sys
import os
			
class ecshop_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '25", "regexp" : '/<title>[^<]+ - Powered by ECShop<\/title>/ },
			{ "version" : '/<meta name="Generator" content="ECSHOP v([\d\.]+)" \/>/ },
		]

