import plugins
			
class Pluginvisec_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<!--wml-->\s+<!--bad-->/" },
			{ "url" : "/favicon.ico", "md5" : "2e5e985fe125e3f8fca988a86689b127" },
			{ "search" : "headers[server]", "version" : "/^VISEC\/([^\s]+)$/" },
		]
	return(self.rules)

