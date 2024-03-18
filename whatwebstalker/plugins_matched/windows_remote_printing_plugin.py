import sys
import os
			
class windows_remote_printing_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'inurl:"Printers/ipp_0001.asp" intitle:"All Printers on"' }
			{ "regexp" : '/<frame src="ipp_000[\d]\.asp\?eprinter=/ }
		]

