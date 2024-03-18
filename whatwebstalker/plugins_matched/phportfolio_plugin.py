import plugins
			
class Pluginphportfolio_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/style="color:gray;font-size:smaller">Powered by <a href="http:\/\/www\.outshine\.com\/phportfolio\/"[^>]*>PHPortfolio<\/a>\./" },
		]
		return(self.rules)
