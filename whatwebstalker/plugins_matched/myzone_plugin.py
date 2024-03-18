import plugins
			
class Pluginmyzone_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<title>MyZone<\/title>.*www\.netcomm\.com\.au/m},
		]
			return(self.rules)
