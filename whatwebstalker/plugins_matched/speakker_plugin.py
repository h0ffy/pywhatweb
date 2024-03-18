import sys
import os
			
class Pluginspeakker_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- INSTANTIATE SPEAKKER -->" },
			{ "text" : "<!-- INCLUDE SPEAKKER -->" },
			{ "regexp" : "/<script type="text\/javascript" src="[^"]+\/(projekktor|speakker)\.min\.js"><\/script>/" },
		]
		return(self.rules)

