import plugins
			
class Pluginphp_nuke_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "module" : /<a href="[^"]*modules.php\?name=([a-zA-Z0-9_]+)[^"]*">/" },
		]
		return(self.rules)
