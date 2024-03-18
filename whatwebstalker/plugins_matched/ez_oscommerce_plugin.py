import plugins
			
class Pluginez_oscommerce_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.eptcel.com.br" target="_blank">ez oscommerce</a>" },
		]
		return(self.rules)

