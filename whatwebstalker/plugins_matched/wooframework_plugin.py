import plugins
			
class Pluginwooframework_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="WooFramework ([\d\.]+)"/" },
		]
	return(self.rules)
