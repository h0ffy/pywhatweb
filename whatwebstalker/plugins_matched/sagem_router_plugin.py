import plugins
			
class Pluginsagem_router_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[www-authenticate]", "regexp" : "/^Basic realm="?Sagem"?$/" },
		]
	return(self.rules)

