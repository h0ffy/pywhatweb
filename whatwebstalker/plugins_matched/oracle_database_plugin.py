import plugins
			
class Pluginoracle_database_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Oracle XML DB\/Oracle Database$/", "module" : "Oracle XML DB" },
		]
		return(self.rules)

