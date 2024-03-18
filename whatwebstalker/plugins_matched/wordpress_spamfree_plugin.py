import plugins
			
class Pluginwordpress_spamfree_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<!-- Protected by \(WP-SpamFree\) v([\d\.]+) :: JS BEGIN -->/" },
		]
			return(self.rules)
