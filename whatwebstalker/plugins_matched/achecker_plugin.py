import plugins
			
class Pluginachecker_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>AChecker : ATRC Accessibility Checker: </title>" },
		]
		return(self.rules)
