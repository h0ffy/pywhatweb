import sys
import os
			
class Pluginpixelpost_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/[Pp]owered by <a href="http:\/\/www.pixelpost.org[\/]?"[\s]*(title="Powered by Pixelpost")?>[Pp]ixel[Pp]ost</" },
			{ "text" : "Powered by <a onclick="window.open(this.href); return false;" href="http://pixelpost.org/" title="Pixelpost">Pixelpost</a>" },
		]

