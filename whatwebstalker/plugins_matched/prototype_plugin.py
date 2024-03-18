import plugins
			
class Pluginprototype_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "js tag", "regexp" : "/<script [^>]*(prototype[^>]*.js)[^>]*},
		]
		return(self.rules)
