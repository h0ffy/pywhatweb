import plugins
			
class Pluginsx_shop_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<a href="http:\/\/www.source-worx.de[^>]+>powered[\s]+by sX-Shop<\/a>/" },
			{ "text" : "<meta name="author" content="Source WorX - Software Development">" },
			{ "text" : "alert("Ihr Suchbegriff muss mind. aus 3 Zeichen bestehen.");" },
		]
			return(self.rules)
