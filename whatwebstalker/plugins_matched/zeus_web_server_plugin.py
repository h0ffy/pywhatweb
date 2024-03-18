import plugins
			
class Pluginzeus_web_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Zeus$/" },
			{ "search" : "headers[server]", "version" : "/^Zeus\/(([\d]+)(\.|_)([\d]+))$/" },
		]
		return(self.rules)
