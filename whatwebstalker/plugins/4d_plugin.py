import plugins
			
class Plugin4d_plugin(plugins.Base):
    def __init__(self):
    	super().__init__()
    	self.rules = []

    def start(self):
        self.rules.append(
			{ "search" : "headers[server]", "version" : "/^4D_v[\d]{1,2}(_SQL)?\/([\d\.]+)$/", "offset" : "1" }
		)
        return self.rules