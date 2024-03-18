import plugins
			
class Pluginwebsocket_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[upgrade]", "regexp" : "/^WebSocket$/i },
			{ "search" : "headers[websocket-location]", "string" : /^(wss?:\/\/.+)/" },
			{ "search" : "headers[sec-websocket-location]", "string" : /^(wss?:\/\/.+)/" },
			{ "search" : "headers[sec-websocket-version-server]", "version" : "/(.+)/" },
			{ "search" : "headers[sec-websocket-protocol]", "module" : /(.+)/" },
		]
			return(self.rules)
