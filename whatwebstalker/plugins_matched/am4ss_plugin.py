import sys
import os
			
class Pluginam4ss_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<meta name="copyright" content="Powered by am4ss ([^\s]+) (Programmed By|programming by) Mohammed Cherkaoui" \/>/" },
			{ "text" : "<!-- Header end and right block start -->" },
			{ "text" : "Powered By <a href="http://am4ss.com"><font color="#FF000">AM4SS</font></a>" },
			{ "regexp" : "/<link rel="stylesheet" type="text\/css" href="templates\/[^\/]+\/am4ss\.css" \/>/" },
		]

