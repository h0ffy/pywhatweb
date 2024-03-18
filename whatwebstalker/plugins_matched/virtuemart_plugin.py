import sys
import os
			
class Pluginvirtuemart_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "25", "regexp" : "/<div id=["']vmMainPage/" },
			{ "certainty" : "75", "text" : "href="/index.php?option=com_virtuemart&amp;page=shop.registration">" },
		]

