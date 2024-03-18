import sys
import os
			
class Pluginchillycms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "	powered by <a href="http://FrozenPepper.de">chillyCMS</a>." },
			{ "text" : "	<p>&copy;2010 <a href=">demo.opensourcecms.com</a>," },
			{ "text" : "	<p>&copy;2010 <a href=">chillycms.bplaced.net</a>," },
		]

