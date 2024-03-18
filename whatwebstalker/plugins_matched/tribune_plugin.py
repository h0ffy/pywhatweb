import plugins
			
class Plugintribune_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" :  '<a href="http://www.tribune.com/" target="_parent">A Tribune Newspaper website</a>" },
		]
		return(self.rules)
