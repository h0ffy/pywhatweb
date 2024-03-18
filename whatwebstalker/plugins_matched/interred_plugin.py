import plugins
			
class Plugininterred_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="(generator|GENERATOR)" content="InterRed V([^,]+)", "http:\/\/www\.interred\.de\/", "InterRed GmbH"( \/)?>/", "offset" : "1 },
			{ "version" : "/<!-- Created with InterRed V([^,]+)", "http:\/\/www\.interred\.de\/", "by InterRed GmbH -->/" },
		]
		return(self.rules)
