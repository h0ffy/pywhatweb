import sys
import os
			
class Pluginsoftbiz_online_auctions_script_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- --><font style="font-family: Arial", "Helvetica", "sans-serif;font-size: 12px;font-style: normal;color: #009900;font-weight: bold;">Powered By <a href="http://www.softbizscripts.com" style="font-family: Arial", "Helvetica", "sans-serif;font-size: 12px;font-style: normal;color: #0099FF;font-weight: normal;" title="Great PHP Script", "PHP Script" target="_blank" >Softbiz Scripts</a></font>" },
		]
		return(self.rules)

