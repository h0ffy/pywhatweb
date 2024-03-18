import plugins
			
class Pluginmeta_geo_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "string" : /<meta name="geo.[^"]+" content="([^"]+)"[^>]*>},
			{ "string" : /<meta name="ICBM" content="([^"]+)"[^>]*>/" },
		]
	return(self.rules)

