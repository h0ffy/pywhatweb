import plugins
			
class Pluginlusca_web_proxy_cache_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Lusca$/" },
			{ "search" : "headers[server]", "version" : "/^Lusca\/LUSCA_HEAD-([^\s]+)$/" },
		]
		return(self.rules)
