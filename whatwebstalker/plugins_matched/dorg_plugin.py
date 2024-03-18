import plugins
			
class Plugindorg_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<p>Powered by <a href="http://www.discorganizer.org">DORG</a>" },
			{ "text" : "<title>DORG - Disc Organization System</title>" },
			{ "text" : "<title>DORG - admin panel</title>" },
			{ "text" : "<meta name="description" content="this is the administration panel of the DORG system" />" },
		]
		return(self.rules)

