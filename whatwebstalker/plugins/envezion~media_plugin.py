import plugins
			
class Pluginenvezion~media_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://envezion.com/">envezion~MEDIA</a>" },
			{ "text" : "Powered by <a href="http://envezion.com/"><strong>envezion~MEDIA</strong></a>" },
			{ "text" : "Powered by <a href="http://www.envezion.com" target="_blank"><strong> envezion~media</strong></a><br />" },
		]
	return(self.rules)
