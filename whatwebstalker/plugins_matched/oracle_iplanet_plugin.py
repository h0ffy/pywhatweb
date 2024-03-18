import sys
import os
			
class oracle_iplanet_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[proxy-agent]", "version" : '/iPlanet-Web-Proxy-Server\/([\d\.]+)/", "module" : 'Proxy" }
			{ "search" : 'headers[server]", "version" : '/iPlanet-WebServer-Enterprise\/([\d\.]+)/", "module" : 'Web" }
			{ "search" : 'headers[server]", "version" : '/Oracle-iPlanet-Web-Server\/([\d\.]+)/", "module" : 'Web" }
		]

