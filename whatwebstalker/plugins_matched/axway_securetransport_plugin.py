import plugins
			
class Pluginaxway_securetransport_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^SecureTransport\/([^\s]+)/" },
			{ "text" : "<!-- /application.bar -->" },
			{ "certainty" : "75", "text" : "<title>Welcome to SecureTransport</title>" },
		]
		return(self.rules)

