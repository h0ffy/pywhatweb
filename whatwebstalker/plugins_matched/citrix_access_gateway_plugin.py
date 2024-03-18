import sys
import os
			
class citrix_access_gateway_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<HTML><HEAD><TITLE>Citrix Access Gateway</TITLE>' }
			{ "text" : '<link rel="SHORTCUT ICON" href="/vpn/images/AccessGateway.ico" type="image/vnd.microsoft.icon">' }
			{ "text" : '<!--CONTENT CONTENT CONTENT CONTENT CONTENT--->' }
			{ "text" : '</div><!---end of div c_logon_maincontent-->' }
			{ "search" : 'headers[set-cookie]", "regexp" : '/ezisneercsresu=/ }
			{ "search" : 'headers[server]", "regexp" : '/^Cyms-SecS v[\d\.]+$/ }
	]
