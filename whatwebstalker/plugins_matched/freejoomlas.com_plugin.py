import sys
import os
			
class Pluginfreejoomlas.com_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Free <a href="http://joomla.org" target=_blank>Joomla!</a> hosting powered by  <a href="http://freejoomlas.com"> FreeJoomlas.com </a>", "module" : "Joomla" },
		]
		return(self.rules)

