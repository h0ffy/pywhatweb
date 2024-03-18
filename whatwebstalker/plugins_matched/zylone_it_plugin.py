import sys
import os
			
class Pluginzylone_it_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered by[:]? <a href="http:\/\/www.zylone.com[\/]*[^>]+>Zylone IT/" },
		]
		return(self.rules)

