import plugins
			
class Pluginfortiweb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^FortiWeb$/" },
			{ "search" : "headers[server]", "version" : "/^FortiWeb-([\d\.]+)$/" },
		]
	return(self.rules)
