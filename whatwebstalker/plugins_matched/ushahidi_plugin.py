import plugins
			
class Pluginushahidi_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "md5" : "7350c3f75cb80e857efa88c2fd136da5", "url" : "/favicon.ico" },
		]
	return(self.rules)
