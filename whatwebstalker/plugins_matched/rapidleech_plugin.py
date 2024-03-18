import sys
import os
			
class Pluginrapidleech_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<small[^>]+>Credits to Pramode &amp; Checkmate &amp; Kloon<\/small><br/" },
			{ "regexp" : "/<small[^>]+>Credits to Pramode &amp; Checkmate &amp; Kloon. Mod by: MsNeil &amp; Idoenk<\/small><br/", "module" : "PlugMod" },
		]
		return(self.rules)

