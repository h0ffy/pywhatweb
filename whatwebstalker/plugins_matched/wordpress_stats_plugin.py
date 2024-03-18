import sys
import os
			
class Pluginwordpress_stats_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/<script src="https?:\/\/(ssl-)?stats\.wordpress\.com\/[^"]+" type="text\/javascript"><\/script>/" },
			{ "regexp" : "/<noscript><img src="https?:\/\/stats\.wordpress\.com\/b\.gif\?v=noscript"/" },
		]

