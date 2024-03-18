import sys
import os
			
class phpcollab_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/^<!-- Powered by PhpCollab v([\d\.]+) \/\/-->$/ }
			{ "version" : '/^<p id="footer">PhpCollab v([\d\.]+)[\s]*<\/p>$/ }
		]

