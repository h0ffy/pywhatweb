import sys
import os
			
class weatimages_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<div align="center" class="weatimages_toppest_navig" style="text-decoration:underline;">' },
			{ "text" : '<meta name="Generator" content="Weatimages"/>' },
			{ "text" : 'Powered by <a href="http://nazarkin.name/projects/weatimages/">Weatimages</a>' },
		]

