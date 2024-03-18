import sys
import os
			
class password_field_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : 'rss link type", "regexp" : '/<input [^>]*?type=["']password["'][^>]*>/i }
		]

