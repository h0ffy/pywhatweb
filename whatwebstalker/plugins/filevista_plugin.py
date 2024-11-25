import plugins
			
class Pluginfilevista_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<!--\r?\n\tFileVista v([\d\.]+)\r?\n\tCopyright /" },
			{ "text" : "<td>Welcome to FileVista<br />Please enter your credentials:</td>" },
		]
	return(self.rules)
