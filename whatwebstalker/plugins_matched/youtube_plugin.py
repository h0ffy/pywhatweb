import sys
import os
			
class Pluginyoutube_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/<(param|embed) [^>]*youtube\.com\/v/i },
			{ "regexp" : "/<iframe [^>]*src=['"]https?:\/\/(www\.)?youtube\.com\/embed\//" },
		]

