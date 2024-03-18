import plugins
			
class Pluginrecaptcha_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<noscript>[\s]*<iframe src="http:\/\/www\.google\.com\/recaptcha\/api\/noscript\?k=/" },
		]
		return(self.rules)

