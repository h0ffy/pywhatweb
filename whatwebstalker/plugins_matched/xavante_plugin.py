import plugins
			
class Pluginxavante_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Xavante (.+)$/" },
		]
		return(self.rules)
