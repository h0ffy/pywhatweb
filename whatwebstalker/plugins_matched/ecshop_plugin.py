import plugins
			
class Pluginecshop_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "regexp" : "/<title>[^<]+ - Powered by ECShop<\/title>/" },
			{ "version" : "/<meta name="Generator" content="ECSHOP v([\d\.]+)" \/>/" },
		]
		return(self.rules)
