import plugins
			
class Plugintwistedweb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/TwistedWeb\/?([^ ]+)?/", "search" : "headers[server]"},
		]
	return(self.rules)

