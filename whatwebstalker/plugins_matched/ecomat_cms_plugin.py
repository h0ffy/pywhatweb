import sys
import os
			
class ecomat_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<meta name="Generator" content="ECOMAT CMS ([\d\.]{1,5})">/" },
		]

