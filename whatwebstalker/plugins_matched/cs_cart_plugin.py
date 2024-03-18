import sys
import os
			
class cs_cart_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '	text_required_group_product: 'Please select a product for the required group [group_name]'," }
			{ "regexp" : '/Powered by <a href="http:\/\/www.cs-cart.com" target="_blank"[^>]+>CS-Cart - Shopping Cart Software<\/a>/ }
			{ "text" : '<title>CS-Cart. Powerful PHP shopping cart software</title>" }
	]

