import plugins
			
class Pluginphp_photo_gallery_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://phpweby.com">PHP Photo Gallery</a>" },
		]
		return(self.rules)
