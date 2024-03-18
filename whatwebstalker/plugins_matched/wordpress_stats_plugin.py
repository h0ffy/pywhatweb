import sys
import os
			
class Pluginwordpress_stats_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script src="https?:\/\/(ssl-)?stats\.wordpress\.com\/[^"]+" type="text\/javascript"><\/script>/" },
			{ "regexp" : "/<noscript><img src="https?:\/\/stats\.wordpress\.com\/b\.gif\?v=noscript"/" },
		]
		return(self.rules)

