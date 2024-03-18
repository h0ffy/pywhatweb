import sys
import os
			
class simsweb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<title>SIMSWeb Loading.....</title>" },
			{ "text" : "index.html"><font color="black" face="arial">Loading SIMSWeb", "please wait.....</font></a></h2>" },
			{ "text" : "<script language="Javascript" src="/SIMSWeb/monitor.js"></script>" },
			{ "text" : "<form onSubmit="sendinfo(); return false;" name="LOGON">" },
		]

