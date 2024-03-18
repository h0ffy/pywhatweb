import sys
import os
			
class php_pro_bid_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/            <div class="version">Current Version:[\r\n]+               ([\d\.]{1,5})            <\/div>[\r\n]+/ }
			{ "regexp" : '/<td colspan="2" bgcolor="#[^"]{3,6}" style="color: #ffffff; font-weight: bold;">PLEASE LOGIN TO THE ADMIN AREA<\/td>/ }
		]

