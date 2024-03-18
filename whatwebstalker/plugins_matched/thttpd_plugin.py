import plugins
			
class Pluginthttpd_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^thttpd\/([^\s]+)/" },
		]
	return(self.rules)
