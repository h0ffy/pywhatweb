import sys
import os
			
class Pluginbrightcove_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/goku\.brightcove\.com|admin\.brightcove\.com\/js},
		]
		return(self.rules)

