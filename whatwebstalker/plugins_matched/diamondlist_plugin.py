import plugins
			
class Plugindiamondlist_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.hulihanapplications.com/projects/diamondlist"><b>DiamondList</b>" },
		]
	return(self.rules)
