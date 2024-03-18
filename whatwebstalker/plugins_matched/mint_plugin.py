import plugins
			
class Pluginmint_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*src=["'][^>]*mint\/\?js/i },
		]
	return(self.rules)

