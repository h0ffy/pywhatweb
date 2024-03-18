import sys
import os
			
class Pluginblackjumbodog_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^BlackJumboDog$/" },
			{ "search" : "headers[server]", "version" : "/^BlackJumboDog Version (.+)$/" },
		]

