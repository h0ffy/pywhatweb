import sys
import os
			
class Pluginstar_network_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered [b|B]+y <a href="http:\/\/www.[starltd.net|s4u.co.il]+[\/]*">Star Network[\ and\ Promotion\ LTD|\&amp\;\ Promotion\ LTD]*<\/a>/" },
		]
		return(self.rules)

