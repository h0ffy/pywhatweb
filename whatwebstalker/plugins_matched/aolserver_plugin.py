import plugins
			
class Pluginaolserver_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^AOLserver$/" },
			{ "search" : "headers[server]", "version" : "/^AOLserver\/([^\s]+)/" },
		]
	return(self.rules)
