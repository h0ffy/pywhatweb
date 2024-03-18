import sys
import os
			
class Pluginfreejoomlas.com_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Free <a href="http://joomla.org" target=_blank>Joomla!</a> hosting powered by  <a href="http://freejoomlas.com"> FreeJoomlas.com </a>", "module" : "Joomla" },
		]

