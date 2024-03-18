import plugins
			
class Pluginrios_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-rbt-optimized-by]", "version" : "/\(RiOS ([^\s]+)\)/" },
			{ "search" : "headers[x-rbt-optimized-by]", "string" : /(.+) \(RiOS/" },
		]
	return(self.rules)
