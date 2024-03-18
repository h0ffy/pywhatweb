import plugins
			
class Pluginclicky_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script[^>]+src=["'](https?:)?\/\/static\.getclicky\.com/i },
		]
		return(self.rules)
