import sys
import os
			
class tab_and_link_manager_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<div id="footer_copyright" class="shade footer_copyright">Powered by <a href="http:\/\/www\.wolfshead-solutions\.com\/ws-products\/product-1" rel="wsBlank">Tab and Link Manager<\/a> Version ([^<^\s]+)<br \/>Copyright &copy; 20[\d]{2} Wolfshead Solutions\. All rights reserved\.<br \/>/ }
		]

