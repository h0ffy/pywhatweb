import plugins
			
class Pluginachecker_plugin(plugins.Base):
    def __init__(self):
        super().__init__()
        self.rules = []

    def start(self):
        self.rules.append({ "text" : "<title>AChecker : ATRC Accessibility Checker: </title>" })
        return self.rules