import sys
import os
			
class tiger_ip_connect_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "search" : 'headers[location]", "regexp" : '/^network\/index\.php$/ }
			{ "version" : '/<title>Tiger IP Connect ([^\s]+) -  Login<\/title>/ }
			{ "text" : '<td align="center" bgcolor="#FFCC00"><b>Login is disabled from this IP address.</b></td>' }
			{ "url" : '/include/tiger.css", "text" : 'background-image:url(../images/tiger/subTabmidden.gif);' }
			{ "text" : '<link rel="stylesheet" href="/include/tms.css">", "string" : 'TigerTMS" }
			{ "text" : '<link rel="stylesheet" href="/include/firedigit.css">", "string" : 'Firedigit" }
		]

