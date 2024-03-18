import plugins
			
class Pluginseminole_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Seminole\/([^\s]+)/" },
		]
		return(self.rules)
