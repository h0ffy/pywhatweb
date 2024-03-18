import sys
import os
			
class Pluginecomat_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<meta name="Generator" content="ECOMAT CMS ([\d\.]{1,5})">/" },
		]

