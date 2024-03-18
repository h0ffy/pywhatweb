import plugins
			
class Pluginsocorro_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://code.google.com/p/socorro/">Socorro</a>" },
		]
	return(self.rules)

