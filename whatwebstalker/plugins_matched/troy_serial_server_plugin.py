import sys
import os
			
class Plugintroy_serial_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "model" : "TROY500", "text" : "<BODY><CENTER><TABLE BORDER=0><TR ALIGN=CENTER><TD><FONT COLOR=RED SIZE=5>TROY Serial Server</FONT></TD></TR>" },
			{ "model" : "TROY500", "text" : "Network Card Access Password&#058; </B><INPUT TYPE=PASSWORD SIZE=16 MAXLENGTH=16 NAME=access_psw>" },
		]

