import plugins
			
class Pluginquantcast_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "quant.js", "regexp" : "/<script[^>]+src=["']http:\/\/edge.quantserve.com\/quant.js["']/" },
		]
	return(self.rules)
