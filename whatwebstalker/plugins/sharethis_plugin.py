import plugins
			
class Pluginsharethis_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*src=["|'][^"^']+w\.sharethis\.com\//i },
		]
	return(self.rules)
