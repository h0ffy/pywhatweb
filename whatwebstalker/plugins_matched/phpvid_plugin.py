import plugins
			
class Pluginphpvid_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div align=\"center\" class='powered_by_a'>Powered By <a href='http://www.vastal.com/' target='_blank' class='powered_by_a'>" },
		]
	return(self.rules)

