import plugins
			
class Pluginbaap_mobile_version_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-mobilized-by]", "version" : "/^BAAP Mobile Version ([^\s]+)$/" },
		]
	return(self.rules)
