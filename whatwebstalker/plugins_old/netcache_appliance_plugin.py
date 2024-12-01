import plugins
			
class Pluginnetcache_appliance_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^NetCache appliance \(NetApp\/([^\)]+)\)$/" },
		]
	return(self.rules)
