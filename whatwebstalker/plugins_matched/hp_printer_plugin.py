import plugins
			
class Pluginhp_printer_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "model" : "/^HP HTTP Server; HP (.+) series - /" },
		]
		return(self.rules)
