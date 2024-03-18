import plugins
			
class Pluginseditio_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="Seditio by Neocrome http://www.neocrome.net" />" },
			{ "text" : "<a href="http://www.neocrome.net">Powered by Seditio</a><br />" },
			{ "text" : "<br />Powered by <a href="http://www.neocrome.net" target="_blank">Seditio</a>" },
		]
	return(self.rules)
