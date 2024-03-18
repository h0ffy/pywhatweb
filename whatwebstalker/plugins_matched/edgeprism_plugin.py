import plugins
			
class Pluginedgeprism_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^EdgePrism\/([^\s]+)$/" },
			{ "search" : "headers[server]", "regexp" : "/^EdgePrismSSL/" },
		]
			return(self.rules)
