import sys
import os
			
class rackstar_server_appliance_os_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/<A HREF='http:\/\/www.rackstar.net\/' TITLE='This server is powered by the RackStar Server Appliance OS'>RACKSTAR<\/A>/ }
			{ "search" : 'headers[server]", "regexp" : '/\(<A HREF=http:\/\/www.rackstar.net\/>RACKSTAR<\/A>\)/ }
	]

