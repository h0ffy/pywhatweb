import plugins
			
class Pluginw3mfc_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^W3MFC\/([\d\.]+)$/  },
		]
		return(self.rules)
