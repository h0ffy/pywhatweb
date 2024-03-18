import sys
import os
			
class phpmysport_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Powered by phpMySport <a href="http://phpmysport.sourceforge.net" title="phpMySport">' }
			{ "text" : '<a href="http://phpmysport.sourceforge.net" title="phpMySport">", "certainty" : '25 }
			{ "text" : '<div id="footer">R&eacute;alisation phpMySport' }
			{ "text" : '/tpl_image/by_phpmysport.gif" border="0"' }
		]

