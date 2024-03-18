import sys
import os
			
class zenoss_core_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<div id="copyright">[\s]+<p>Copyright &copy; 2005-20[\d]{2} Zenoss", "Inc\. \| Version[\s]+<span>([^\s^<]+)<\/span>[\s]+/ }
			{ "text" : '<link rel="shortcut icon" type="image/x-icon" href="/zport/dmd/favicon.ico" />' }
	]

