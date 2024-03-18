import plugins
			
class Pluginintrasrv_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^intrasrv ([\d\.]+)$/" },
		]
		return(self.rules)
