import plugins
			
class Pluginusp_secure_entry_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Secure Entry Server$/" },
		]
		return(self.rules)
