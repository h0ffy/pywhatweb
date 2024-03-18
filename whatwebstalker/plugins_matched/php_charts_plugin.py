import sys
import os
			
class Pluginphp_charts_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "regexp" : "/\b(href|src)\s*=\s*["'][^>]*url\.php\?type=bar&dimension=[^\s^&]+&data_type=[^\s^&]+&file_path=[^&]+&group_col=[^\s^&]+&series_col=[^\s^&]+&output_type=[^\s^&]+/" },
		]
		return(self.rules)

