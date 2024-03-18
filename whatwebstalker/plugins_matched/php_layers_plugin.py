import plugins
			
class Pluginphp_layers_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "Powered by PHP Layers"" },
			{ "text" : "// because Konqueror 3 sets IE = 1 ... AAAAAAAAAARGHHH!!!" },
			{ "text" : ".png" alt="Powered by PHP Layers Menu" height="31" width="88" /></a>" },
			{ "version" : "/<!-- end of menu header - PHP Layers Menu ([^\s]+) \(C\) [0-9]{4}-[0-9]{4} Marco Pratesi/" },
			{ "version" : "/\/\/ PHP Layers Menu ([^\s]+) \(C\) [0-9]{4}-[0-9]{4} Marco Pratesi/" },
		]
	return(self.rules)
