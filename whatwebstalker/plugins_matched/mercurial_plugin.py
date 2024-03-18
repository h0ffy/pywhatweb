import sys
import os
			
class Pluginmercurial_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<a href="http://mercurial.selenic.com/" title="Mercurial" style="float: right;">Mercurial</a>" },
			{ "regexp" : "/<div id="powered-by">[\s]+<p><a href="http:\/\/mercurial\.selenic\.com\/" title="Mercurial">/" },
		]

