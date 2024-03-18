import sys
import os
			
class Pluginclicktale_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="ClickTaleDiv" style="display: none;"></div>" },
		]
		return(self.rules)

