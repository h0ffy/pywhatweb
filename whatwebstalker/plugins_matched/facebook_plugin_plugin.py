import plugins
			
class Pluginfacebook_plugin_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "string" : /<i?frame[^>]+src[\s]*="http:\/\/(www|apps)\.facebook.com\/plugins\/([^\.^\/^\?]+)\.php\?/i", "offset" : "1 },
		]
		return(self.rules)
