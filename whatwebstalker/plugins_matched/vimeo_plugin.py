import plugins
			
class Pluginvimeo_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<(param|object|embed) [^>]+vimeo\.com\/moogaloop/i },
			{ "regexp" : "/<iframe [^>]*src=['"]https?:\/\/player\.vimeo\.com\/video\//" },
		]
	return(self.rules)
