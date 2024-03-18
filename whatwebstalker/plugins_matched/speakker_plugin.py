import sys
import os
			
class speakker_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- INSTANTIATE SPEAKKER -->' }
			{ "text" : '<!-- INCLUDE SPEAKKER -->' }
			{ "regexp" : '/<script type="text\/javascript" src="[^"]+\/(projekktor|speakker)\.min\.js"><\/script>/ }
		]

