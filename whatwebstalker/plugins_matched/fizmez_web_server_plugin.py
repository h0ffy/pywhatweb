import plugins
			
class Pluginfizmez_web_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Fizmez\/0\.0\.1/", "version" : "1.0" },
			{ "search" : "headers[server]", "version" : "/^Fizmez\/([1-9]+\.[\d\.]+)/" },
		]
		return(self.rules)
