import sys
import os
			
class Pluginmercurial_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a href="http://mercurial.selenic.com/" title="Mercurial" style="float: right;">Mercurial</a>" },
			{ "regexp" : "/<div id="powered-by">[\s]+<p><a href="http:\/\/mercurial\.selenic\.com\/" title="Mercurial">/" },
		]
		return(self.rules)

