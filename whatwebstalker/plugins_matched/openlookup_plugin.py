import plugins
			
class Pluginopenlookup_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<h2>OpenLookup Node Status</h2>" },
			{ "version" : "/<p><a href="http:\/\/openlookup\.googlecode\.com\/">Source code and\n	further information<\/a> are available\.  This is OpenLookup V([^<]+)\.<\/p>/" },
		]
		return(self.rules)
