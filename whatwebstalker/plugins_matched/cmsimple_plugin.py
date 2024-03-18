import plugins
			
class Plugincmsimple_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "Powered by CMSimple.dk" welcome", "certainty" : "75 },
			{ "text" : "<meta name="generator" content="CMSimple" },
			{ "version" : "/<meta name="generator" content="CMSimple ([\d\.]+)[^>]*>/" },
		]
		return(self.rules)
