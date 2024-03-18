import sys
import os
			
class cpcommerce_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '        Powered by cpCommerce' }
			{ "text" : '    <title>cpCommerce by Matthew Wilkin</title>' }
			{ "text" : 'Powered by <a href="http://cpcommerce.cpradio.org/" target="_blank">cpCommerce</a>.' }
			{ "text" : 'Powered by <a href="http://cpcommerce.org/" target="_blank">cpCommerce</a>.' }
	]

