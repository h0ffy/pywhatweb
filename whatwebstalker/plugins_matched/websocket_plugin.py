import sys
import os
			
class websocket_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[upgrade]", "regexp" : '/^WebSocket$/i }
			{ "search" : 'headers[websocket-location]", "string" : /^(wss?:\/\/.+)/ }
			{ "search" : 'headers[sec-websocket-location]", "string" : /^(wss?:\/\/.+)/ }
			{ "search" : 'headers[sec-websocket-version-server]", "version" : '/(.+)/ }
			{ "search" : 'headers[sec-websocket-protocol]", "module" : /(.+)/ }
		]

