import sys
import os
			
class Pluginez_oscommerce_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.eptcel.com.br" target="_blank">ez oscommerce</a>" },
		]

