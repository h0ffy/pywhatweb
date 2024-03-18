import plugins
			
class Pluginwstool_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<a href="http:\/\/sourceforge\.net\/projects\/wstool" target="_blank">Server Error & SQL Injection Sacnner \(Ver ([^\s^\)]+)\)<\/a>/" },
			{ "version" : "/<title>Server Error & SQL Injection Sacnner \(Ver ([^\s^\)]+)\)<\/title>/" },
		]
		return(self.rules)
