import plugins
			
class Pluginmicrosys_promotic_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Promotic$/" },
			{ "text" : "<html><head><title>PROMOTIC Redirection</title></head>" },
		]
	return(self.rules)

