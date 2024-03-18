import plugins
			
class Pluginwordpress_mobile_pack_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-mobilized-by]", "version" : "/^WordPress Mobile Pack ([^\s]+)$/" },
		]
		return(self.rules)

