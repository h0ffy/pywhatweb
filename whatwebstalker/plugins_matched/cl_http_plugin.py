import plugins
			
class Plugincl_http_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^CL-HTTP\/([^\s]+)/" },
			{ "search" : "headers[server]", "string" : /^CL-HTTP\/[^\s]+ \(([^\)]+)\)/" },
		]
		return(self.rules)
