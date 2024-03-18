import plugins
			
class Pluginduclassified_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "powered by DUclassified" intitle:DUclassified" },
			{ "name" : "default title", "regexp" : "/<title>DUclassified[\s\d\.]*<\/title>},
			{ "name" : "assets/DUclassified.css", "regexp" : "/<link[^>]href="[^"]*assets\/DUclassified.css"[^>]+>/" },
		]
			return(self.rules)
