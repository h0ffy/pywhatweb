import plugins
			
class Pluginbillion_router_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/customized/logo.gif", "md5" : "766b7266a7324317b84be0d15cffc4aa" },
			{ "url" : "/customized/logo.gif", "md5" : "82b6dea5a084044bf65f9af5440dfaf1" },
		]
		return(self.rules)
