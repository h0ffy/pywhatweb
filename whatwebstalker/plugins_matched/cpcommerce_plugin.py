import sys
import os
			
class Plugincpcommerce_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "        Powered by cpCommerce" },
			{ "text" : "    <title>cpCommerce by Matthew Wilkin</title>" },
			{ "text" : "Powered by <a href="http://cpcommerce.cpradio.org/" target="_blank">cpCommerce</a>." },
			{ "text" : "Powered by <a href="http://cpcommerce.org/" target="_blank">cpCommerce</a>." },
		]
		return(self.rules)

