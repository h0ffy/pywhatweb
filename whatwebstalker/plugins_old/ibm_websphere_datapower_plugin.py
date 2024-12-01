import plugins
			
class Pluginibm_websphere_datapower_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-backside-transport]", "string" : /(FAIL|OK)/" },
		]
	return(self.rules)
