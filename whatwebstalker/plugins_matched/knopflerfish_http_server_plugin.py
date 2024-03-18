import plugins
			
class Pluginknopflerfish_http_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^The Knopflerfish HTTP Server$/" },
		]
		return(self.rules)
