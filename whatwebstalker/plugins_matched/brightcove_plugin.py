import sys
import os
			
class Pluginbrightcove_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/goku\.brightcove\.com|admin\.brightcove\.com\/js},
		]

