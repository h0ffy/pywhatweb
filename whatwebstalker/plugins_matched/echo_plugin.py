import sys
import os
			
class Pluginecho_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/<a href="http:\/\/www\.helloecho\.com\/go\/\?[^"]*" target="_blank">powered by echo<\/a>},
		]

