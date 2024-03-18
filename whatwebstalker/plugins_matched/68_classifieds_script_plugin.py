import plugins
			
class Plugin68_classifieds_script_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.68classifieds.com">68 Classifieds Script</a>" },
			{ "version" : "/<meta name="author" content="68 Classifieds - v([^"]+)" \/>/" },
		]
		return(self.rules)

