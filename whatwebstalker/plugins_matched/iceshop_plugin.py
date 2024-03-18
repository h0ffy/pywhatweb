import sys
import os
			
class iceshop_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<p id="power_by"><a href="http://www.iceshop.nl" target="_blank">Powered by ICEshop</a></p>' }
			{ "text" : 'Powered by <a class="link copyright02" href="http://www.iceshop.nl/" target="_blank">ICEshop</a>' }
			{ "text" : '<dl class="box boxLogo  box02 iceshop">' }
		]

