import sys
import os
			
class Pluginclicktale_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<div id="ClickTaleDiv" style="display: none;"></div>" },
		]

