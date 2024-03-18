import plugins
			
class Pluginchillycms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "	powered by <a href="http://FrozenPepper.de">chillyCMS</a>." },
			{ "text" : "	<p>&copy;2010 <a href=">demo.opensourcecms.com</a>," },
			{ "text" : "	<p>&copy;2010 <a href=">chillycms.bplaced.net</a>," },
		]
	return(self.rules)

