import plugins


class Pluginvigor_router_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"search": "headers[server]", "model": "/^(VigorAccess) Web Server$/"},
			{"search": "headers[www-authenticate]", "model": "/^Basic realm="(Login to)?Vigor([\d]+)"$/", "offset" : "1 },
		]
	return(self.rules)
