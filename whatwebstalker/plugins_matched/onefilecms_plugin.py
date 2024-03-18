import sys
import os
			
class onefilecms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<p>This site powered by <a href="http://onefilecms.com/">OneFileCMS</a>. [<a href="onefilecms.php?f=index.php">Admin</a>]</p>' }
	]

