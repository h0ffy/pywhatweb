import sys
import os
			
class Pluginth_erp_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<LINK REL=StyleSheet HREF='../include/therp.css' TYPE='text/css'><script>" },
			{ "text" : "<title>thERP - Login</title>" },
		]
		return(self.rules)

