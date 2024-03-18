import sys
import os
			
class hostbill_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- part below is not css valid. remove it if you want this document to be css valid -->' },
			{ "text" : '</div><br/><center>Powered by <a href="http://hostbillapp.com" target="_blank"><strong>HostBill</strong></a></center><br/></div>' },
		]

