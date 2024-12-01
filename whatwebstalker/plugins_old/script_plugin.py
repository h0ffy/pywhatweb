import plugins
			
class Pluginscript_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script(\s|>)/i },
			{ "string" : /<script[^>]+(language|type)\s*=\s*['"]?([^'"\s]+)['"]?/", "offset" : "1 },
		]
	return(self.rules)
