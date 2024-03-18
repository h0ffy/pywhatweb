import sys
import os
			
class epic_web_honeypot_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<center><font size="3" face="monospace">******************************** Epic Web Honeypot ********************************</font></center>' }
			{ "version" : '/<center><font size="3" face="monospace">\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Version ([^\s]+) \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*<\/font><\/center>/ }
			{ "text" : '<!-- Added OS fingerprints - creds - nmap and honeyd nmap.prints file!-->' }
		]

