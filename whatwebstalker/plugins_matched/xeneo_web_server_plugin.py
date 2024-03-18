import plugins
			
class Pluginxeneo_web_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Xeneo\/([^\s]+)$/" },
			{ "search" : "headers[server]", "regexp" : "/^Xeneo$/" },
		]
		return(self.rules)
