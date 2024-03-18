import sys
import os
			
class Pluginspree_commerce_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>" },
		]
		return(self.rules)

