import plugins
			
class Pluginphpmybible_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div class='randomverse'>" },
			{ "text" : "<div class='fleft'><div class='chaphead'>" },
		]
	return(self.rules)

