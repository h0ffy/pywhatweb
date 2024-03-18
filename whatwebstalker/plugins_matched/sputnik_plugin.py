import plugins
			
class Pluginsputnik_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href='http://sputnik.freewisdom.org/'>Sputnik</a>" },
			{ "text" : "Powered by <a href='http://spu.tnik.org/'>Sputnik</a>" },
		]
		return(self.rules)
