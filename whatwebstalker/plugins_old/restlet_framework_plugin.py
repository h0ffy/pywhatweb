import plugins
			
class Pluginrestlet_framework_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Restlet-Framework\/([^\s]+)$/" },
		]
	return(self.rules)
