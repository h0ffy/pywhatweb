import sys
import os
			
class dv_cart_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<div id="KT_tngdeverror"><label>Message:</label><div>You must have the proper credentials to access this page. Please login.</div></div>' }
			{ "text" : '<table cellpadding="2" cellspacing="0" class="KT_tngtable">' }
		]

