import sys
import os
			
class Plugincomprafacil_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a id="seloPowered" href="http://www.comprafacil.com.br"><img alt="Powered by Comprafacil" src="" },
			{ "text" : "<meta name="author"      content="HERMES SA" />" },
			{ "text" : "<meta name="author" content="HERMES SA" />" },
		]
		return(self.rules)

