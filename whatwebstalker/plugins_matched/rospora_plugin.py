import plugins
			
class Pluginrospora_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<link rel="Shortcut Icon" href="img/wowlogoanim.gif" type="image/gif">" },
			{ "text" : "<li>This server supports only 2.2.3 clients<br><li>1x Quest XP ", "1x Kill XP ", "1x Discovery XP" },
		]
		return(self.rules)
