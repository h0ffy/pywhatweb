import plugins
			
class Pluginiqeye_netcam_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "model" : "/<title>IQeye([^:]+): Live Images[^<]*<\/title>/i },
		]
	return(self.rules)

