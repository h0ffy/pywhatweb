import plugins
			
class Plugintinybb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Proudly powered by <a href='http://tinybb.net'>TinyBB</a>" },
		]
		return(self.rules)
