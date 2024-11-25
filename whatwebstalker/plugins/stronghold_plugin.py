import plugins
			
class Pluginstronghold_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Stronghold$/" },
			{ "search" : "headers[server]", "version" : "/^Stronghold\/([^\s]+)/" },
			{ "search" : "headers[server]", "string" : /(C2Net[A-Z]{2}\/[^\s]+)/" },
		]
	return(self.rules)
