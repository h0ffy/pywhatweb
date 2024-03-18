import plugins
			
class Plugindeluge_web_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<title>Deluge: Web UI ([^<]+)<\/title>},
		]
		return(self.rules)
