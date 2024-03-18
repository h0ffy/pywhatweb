import sys
import os
			
class interspire_shopping_cart_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "	<meta name="generator" content="Interspire Shopping Cart" />" },
			{ "regexp" : "/				Powered by <a href="http:\/\/www.interspire.com\/shoppingcart[\/]*" target="_blank" class="PoweredBy">Interspire Shopping Cart<\/a>/" },
		]

