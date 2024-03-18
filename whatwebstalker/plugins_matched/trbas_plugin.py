import plugins
			
class Plugintrbas_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" :  '<link rel="stylesheet" href="http://www.trbas.com" },
		]
	return(self.rules)

