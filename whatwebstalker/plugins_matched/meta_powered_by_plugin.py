import plugins
			
class Pluginmeta_powered_by_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "string" : /<meta[^>]+name=["']powered[\- ]?by["'][^>]+content=["']([^"]+)["']/i },
		]
	return(self.rules)

