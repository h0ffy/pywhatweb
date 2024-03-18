import sys
import os
			
class Pluginphp_photo_gallery_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://phpweby.com">PHP Photo Gallery</a>" },
		]
		return(self.rules)

