import plugins
			
class Pluginrcttools_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^RCTTools \(SecureSOHO Web configuration Tools\) v([^\s]+)$/" },
		]
			return(self.rules)
