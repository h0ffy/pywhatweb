import plugins
			
class Plugindxsock_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^RemObjects DXSock Web Server/" },
			{ "search" : "headers[user-agent]", "regexp" : "/^RemObjects SDK$/" },
		]
		return(self.rules)
