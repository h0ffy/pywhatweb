import plugins
			
class Pluginpowerschool_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^PowerSchool$/" },
		]
		return(self.rules)
