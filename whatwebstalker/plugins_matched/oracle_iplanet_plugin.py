import plugins
			
class Pluginoracle_iplanet_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[proxy-agent]", "version" : "/iPlanet-Web-Proxy-Server\/([\d\.]+)/", "module" : "Proxy" },
			{ "search" : "headers[server]", "version" : "/iPlanet-WebServer-Enterprise\/([\d\.]+)/", "module" : "Web" },
			{ "search" : "headers[server]", "version" : "/Oracle-iPlanet-Web-Server\/([\d\.]+)/", "module" : "Web" },
		]
		return(self.rules)
