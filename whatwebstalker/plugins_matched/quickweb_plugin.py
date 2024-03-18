import plugins
			
class Pluginquickweb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<HTML><HEAD><TITLE>QWScript Error</TITLE></HEAD>" },
		]
		return(self.rules)
