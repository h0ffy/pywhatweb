import plugins
			
class Pluginaddthis_plugin(plugins.Base):
    def __init__(self):
    	self.rules = []
    	
    def start(self):
        self.rules.append(
			{ "regexp" : r"/<script [^>]*src=[\"|'][^>]*addthis\.com\/js/i" }
		)
        return self.rules