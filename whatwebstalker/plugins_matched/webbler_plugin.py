import plugins
			
class Pluginwebbler_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="webbler ([^\s]+) - http:\/\/tincan\.co\.uk\/webbler"  \/?>/" },
		]
		return(self.rules)
