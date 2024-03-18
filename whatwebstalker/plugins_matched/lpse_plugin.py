import plugins
			
class Pluginlpse_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[location]", "regexp" : "/^(https?:\/\/[^\/]+)?\/eproc\/app/" },
			{ "text" : "<link rel="stylesheet" type="text/css" href="/eproc/assets/application.css"/>" },
		]
		return(self.rules)
