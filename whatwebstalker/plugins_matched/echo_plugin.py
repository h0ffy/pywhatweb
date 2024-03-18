import plugins
			
class Pluginecho_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<a href="http:\/\/www\.helloecho\.com\/go\/\?[^"]*" target="_blank">powered by echo<\/a>},
		]
		return(self.rules)
