import sys
import os
			
class slingbox_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[set-cookie]", "regexp" : '/_sling_skey=[^;]+/ },
			{ "version" : '/<!-- Footer start -->\s+<div id="footer_center">\s+<p>Portal Version:&nbsp;([^,]+)", "Plugin Version:&nbsp;/ },
		]

