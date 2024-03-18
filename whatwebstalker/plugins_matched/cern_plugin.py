import plugins
			
class Plugincern_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^CERN\/([^\s]+)/" },
		]
			return(self.rules)
