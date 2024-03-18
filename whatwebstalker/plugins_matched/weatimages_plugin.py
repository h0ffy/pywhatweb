import sys
import os
			
class Pluginweatimages_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div align="center" class="weatimages_toppest_navig" style="text-decoration:underline;">" },
			{ "text" : "<meta name="Generator" content="Weatimages"/>" },
			{ "text" : "Powered by <a href="http://nazarkin.name/projects/weatimages/">Weatimages</a>" },
		]
		return(self.rules)

