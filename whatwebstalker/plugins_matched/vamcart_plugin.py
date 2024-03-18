import sys
import os
			
class vamcart_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<link type="text\/css" href="[^"]+\/stylesheets\/load\/vamcart\.css" rel="stylesheet"  media="screen"\/>/ }
			{ "text" : '<!-- Powered by: VamCart (http://vamcart.com) -->' }
			{ "text" : '<p><a href="http://vamcart.com/">PHP Shopping Cart</a> <a href="http://vamcart.com/">VamCart</a></p>' }
		]

