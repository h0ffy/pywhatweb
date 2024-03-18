import plugins
			
class Pluginframe_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<i?frame\s+/i },
		]
		return(self.rules)
