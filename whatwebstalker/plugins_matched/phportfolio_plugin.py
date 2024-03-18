import sys
import os
			
class phportfolio_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/style="color:gray;font-size:smaller">Powered by <a href="http:\/\/www\.outshine\.com\/phportfolio\/"[^>]*>PHPortfolio<\/a>\./ },
		]

