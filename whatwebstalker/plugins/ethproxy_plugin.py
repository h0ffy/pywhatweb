import plugins
			
class Pluginethproxy_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^ethProxy$/" },
		]
	return(self.rules)
