import sys
import os
			
class Pluginwordpress_contact_form_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<input type="hidden" name="_wpcf([\d\.]+)" value="1" \/>/" },
		]

