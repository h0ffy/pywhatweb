import plugins
			
class Pluginnetgear_firewall_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^NETGEAR Firewall$/" },
		]
	return(self.rules)
