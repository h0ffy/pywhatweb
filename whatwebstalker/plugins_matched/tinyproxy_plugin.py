import plugins
			
class Plugintinyproxy_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^tinyproxy\/([^\s]+)/" },
		]
		return(self.rules)
