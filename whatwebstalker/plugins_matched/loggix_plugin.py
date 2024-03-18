import plugins
			
class Pluginloggix_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="Loggix" />" },
			{ "version" : "/Powered by <a href="http:\/\/loggix.gotdns.org">Loggix<\/a> ver.([\d\.]+)<\/address>/" },
		]
	return(self.rules)

