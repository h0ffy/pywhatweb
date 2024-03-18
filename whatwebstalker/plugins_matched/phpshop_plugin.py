import plugins
			
class Pluginphpshop_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "regexp" : "/Powered by phpShop/i },
			{ "regexp" : "/Powered by <a href="http:\/\/www.phpshop.org"[^>]*>phpShop<\/a>/i },
			{ "version" : "/Powered by <a href="http:\/\/www.phpshop.org"[^>]*>phpShop<\/a>[\r\n\s]+([\d\.]+) /" },
		]
		return(self.rules)
