import plugins
			
class Pluginswiki_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/defaultScheme/comSwiki.gif", "md5" : "81d538bed9f676fffbdaedb9d95cdbc1" },
		]
	return(self.rules)
