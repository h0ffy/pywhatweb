import plugins
			
class Pluginakamai_global_host_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^AkamaiGHost/" },
		]
			return(self.rules)
