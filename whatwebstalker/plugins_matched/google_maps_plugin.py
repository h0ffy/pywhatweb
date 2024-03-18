import plugins
			
class Plugingoogle_maps_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*src=["'][^>]*maps\.google\.com\/maps(\?file=api|\/api\/staticmap)/i },
		]
		return(self.rules)

