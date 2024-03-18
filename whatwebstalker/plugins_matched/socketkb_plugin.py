import plugins
			
class Pluginsocketkb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/>Powered by SocketKB version ([\d\.]+)<\/a>/" },
		]
		return(self.rules)
