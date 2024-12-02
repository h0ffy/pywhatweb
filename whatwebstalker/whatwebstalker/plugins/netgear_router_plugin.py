import plugins


class Pluginnetgear_router_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"regexp": "/^Basic realm="?[\s]*Netgear/", "certainty" : "75", "search" : "headers[www-authenticate]" },
			{ "model" : "/^Basic realm="?[\s]*NETGEAR ([^"]+)[\s]*"?/", "certainty" : "75", "search" : "headers[www-authenticate]" },
		]
	return(self.rules)
