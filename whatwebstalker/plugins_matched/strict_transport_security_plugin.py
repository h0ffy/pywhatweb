import plugins
			
class Pluginstrict_transport_security_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[Strict-Transport-Security]", "string" : /^(.*)$/" },
		]
		return(self.rules)
