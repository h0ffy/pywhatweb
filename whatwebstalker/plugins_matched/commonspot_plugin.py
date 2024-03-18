import plugins
			
class Plugincommonspot_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<meta[^>]+name="Generator"[^>]+content="CommonSpot[^"]+"[^>]*\/>/" },
			{ "regexp" : "/<img[^>]+src="[^"]+commonspot[^"]+"[^>]*\/>/" },
			{ "regexp" : "/<link[^>]+href="[^"]commonspot\/commonspot\.css"[^>]+\/>/" },
			{ "version" : "/<meta[^>]+name="Generator"[^>]+content="CommonSpot[^\d^"]+([\d\.]+)"[^>]*\/>/" },
		]
	return(self.rules)

