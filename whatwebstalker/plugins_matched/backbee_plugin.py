import plugins
			
class Pluginbackbee_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "100", "text" : "<div id="bb5-site-wrapper">" },
		]
		return(self.rules)
