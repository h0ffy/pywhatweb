import sys
import os
			
class Pluginonefilecms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<p>This site powered by <a href="http://onefilecms.com/">OneFileCMS</a>. [<a href="onefilecms.php?f=index.php">Admin</a>]</p>" },
		]
		return(self.rules)

