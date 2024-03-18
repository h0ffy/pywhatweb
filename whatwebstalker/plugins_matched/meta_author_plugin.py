import plugins
			
class Pluginmeta_author_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "string" : /<meta[^>^=]+name[\s]*=[\s]*['"]?author['"]?[^>^=]+content[\s]*=[\s]*['"]([^'^"^>]+)/i },
			{ "string" : /<meta[^>^=]+content[\s]*=[\s]*['"]([^"^'^>]+)['"][^>^=]+name[\s]*=[\s]*['"]?author['"]?/i },
		]
		return(self.rules)
