import sys
import os
			
class pithcms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<p class="admin">Powered by <a href="http://pithcms.altervista.org/index.php?pagina=data/info.php">PithCMS</a>' }
			{ "text" : '/icons/admin48.png"><br />Welcome Admin.<br /><br />", "path" : 'login.asp' }
		]

