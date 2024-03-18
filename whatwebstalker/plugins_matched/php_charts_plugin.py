import sys
import os
			
class php_charts_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : "25", "regexp" : "/\b(href|src)\s*=\s*["'][^>]*url\.php\?type=bar&dimension=[^\s^&]+&data_type=[^\s^&]+&file_path=[^&]+&group_col=[^\s^&]+&series_col=[^\s^&]+&output_type=[^\s^&]+/" },
		]

