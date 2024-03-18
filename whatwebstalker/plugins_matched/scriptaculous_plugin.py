import plugins
			
class Pluginscriptaculous_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*(scriptaculous[^>]*.js)[^>]*},
		]
		return(self.rules)
