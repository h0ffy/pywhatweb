import sys
import os
			
class Pluginwordfusion_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/<head id="Head"><title>\s+WordFusion\.Web\s+\<\/title>/" },
			{ "text" : "<param name="source" value="ClientBin/WordFusion.Web.xap">" },
		]

