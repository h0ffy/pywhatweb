import plugins
			
class Pluginaccess_control_allow_methods_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[access-control-allow-methods]", "string" : /(.+)/" },
		]
	return(self.rules)

