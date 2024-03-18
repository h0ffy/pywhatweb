import sys
import os
			
class pnpscada_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<TITLE>Welcome to Plug and Play Scada</TITLE>" },
			{ "text" : "<TITLE>Login - PnPSCADA</TITLE>" },
			{ "version" : "/<CENTER><SPAN style='font-family:arial;font-size:10px'>PNPSCADA ([^\s]+) &copy;20[\d]{2} SDG Technologies cc\. All rights strictly reserved\. Please review our <A target='_blank' style='font-family:arial;font-size:10px' href='termsandconditions\.html'>Terms and Conditions<\/A>\. <\/SPAN><\/CENTER>/" },
		]

