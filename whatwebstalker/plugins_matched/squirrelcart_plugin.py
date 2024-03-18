import sys
import os
			
class squirrelcart_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<div class="sc_link">Powered by <a target="_blank" href="http://www.squirrelcart.com/php_shopping_cart.php">Squirrelcart &copy; PHP Shopping Cart Software</a></div>' }
			{ "text" : '<!-- Template: price_html.tpl.php -->' }
			{ "version" : '/<title>Squirrelcart v([^\s]+) Control Panel<\/title>/ }
			{ "search" : 'headers[set-cookie]", "regexp" : '/SC_referer=}
			{ "search" : 'headers[set-cookie]", "regexp" : '/SC_referral_date=[\d]{4}\-[0-1][\d]\-[0-3][\d]\+/ }
	]

