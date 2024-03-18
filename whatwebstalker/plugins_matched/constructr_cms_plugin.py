import sys
import os
			
class Pluginconstructr_cms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<html><head><title>Constructr CMS</title><body><p>Sorry", "no Workspace-Template found!</p><p>Visit <a href="http://constructr.phaziz.com">http://constructr.phaziz.com</a> for further Information.</p></body></head>" },
			{ "text" : "<br /><br />Constructr CMS - developed by <a href="http://phaziz.com/constructr-cms/" onclick="window.open(this.href);return false;">phaziz interface design</a>" },
		]
		return(self.rules)

