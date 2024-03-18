import plugins
			
class Pluginzen_load_balancer_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/config/global.conf", "version" : "/#version ZEN\s+\$version=\"([^\"]+)"/" },
			{ "search" : "headers[www-authenticate]", "text" : "Basic realm="Zen Load Balancer"" },
		]
	return(self.rules)

