import plugins
			
class Pluginairtiesrouter_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<title>Airties ([^<]+)<},
		]
			return(self.rules)
