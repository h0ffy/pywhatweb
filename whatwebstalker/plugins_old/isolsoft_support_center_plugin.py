import plugins
			
class Pluginisolsoft_support_center_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<strong><font color="#FF0000">Warning! This heldesk requires a browser with javascript " },
			{ "text" : "<!-- Copyright Line: Unauthorized removal can void license -->" },
			{ "version" : "/<p align="center"><font size="1">Powered by: Support Center v([^<^\s]+)<br>/" },
		]
	return(self.rules)
