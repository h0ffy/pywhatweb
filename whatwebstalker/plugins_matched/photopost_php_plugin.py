import sys
import os
			
class photopost_php_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>PhotoPost Administration Menu</title>' },
			{ "text" : '<frame name="mainFrame"  src="adm-misc.php?admact=mainmenu" scrolling="yes" frameborder="0" marginwidth="0" marginheight="0" border="no" />' },
			{ "text" : 'Powered by: <a target="_blank" href="http://www.photopost.com">PhotoPost</a> PHP<br />' },
			{ "text" : 'Powered by: <a target="_blank" href="http://www.photopost.com">PhotoPost</a> PHP vB3 Enhanced<br />' },
			{ "text" : ' - Powered by PhotoPost</title>' },
		]

