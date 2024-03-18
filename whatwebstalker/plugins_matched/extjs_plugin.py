import plugins
			
class Pluginextjs_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*src=["'][^>]*ext\-base\.js["']/i },
		]
	return(self.rules)

