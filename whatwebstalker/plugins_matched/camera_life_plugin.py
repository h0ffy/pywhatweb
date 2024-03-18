import sys
import os
			
class camera_life_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<meta name="generator" content="Camera Life version ([^"]+)">},
			{ "string" : "<a href="http://fulldecent.github.io/cameralife"><i class="fa fa-globe"></i> Built with Camera Life</a>'},
			{ "version" : "/This site is powered by Camera Life version ([^ ]+)},
		]

