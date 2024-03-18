import plugins
			
class Pluginapache_wicket_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "inurl:"wicket:bookmarkablePage=:"" },
		]
	return(self.rules)
