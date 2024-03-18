import plugins
			
class Pluginextplorer_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/extplorer.xml", "version" : "/<version>([^<]+)<\/version>/" },
			{ "text" : "<title>Login - eXtplorer</title>" },
		]
		return(self.rules)
