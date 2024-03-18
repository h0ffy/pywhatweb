import plugins
			
class Pluginliteradius_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "inurl:locator.php parsed_page lat long" },
		]
		return(self.rules)
