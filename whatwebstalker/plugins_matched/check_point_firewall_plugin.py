import sys
import os
			
class check_point_firewall_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[location]", "regexp" : '/\/fwauthredirect[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}id[\d]+$/ }
			{ "status" : '401", "string" : /FW-1 at ([^\s]+): Unauthorized to access the document\./ }
	]

