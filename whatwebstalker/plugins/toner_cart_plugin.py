import plugins
			
class Plugintoner_cart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<p align="right"><font color="#FFFFFF">Powered by <a href="http://www.vastal.com/" target="_blank"><font color="#FFFFFF">Vastal I-Tech" },
		]
	return(self.rules)
