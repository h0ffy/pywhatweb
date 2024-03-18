import plugins
			
class Pluginlightbox_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script [^>]*(lightbox[^>]*.js)[^>]*},
		]
	return(self.rules)
