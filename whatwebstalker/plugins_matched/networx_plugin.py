import plugins
			
class Pluginnetworx_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.socialabc.com">NetworX</a>" },
		]
		return(self.rules)
