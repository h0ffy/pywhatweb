import plugins
			
class Pluginraidenhttpd_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^RaidenHTTPD\/([^\s]+) \([^\)]+\)$/" },
			{ "search" : "headers[server]", "string" : /^RaidenHTTPD\/[^\s]+ \(([^\)]+)\)$/" },
		]
	return(self.rules)
