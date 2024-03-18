import sys
import os
			
class Pluginpixel_script_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<font color=#8888888 style="font-size:9px">Powered by <a href="http:\/\/www.texmedia.de" target="_blank" style="color:#888888;font:normal;text-decoration:none">(Million )?Pixel Script<\/a> v?([^&]+) &copy; <a href="http:\/\/www.texmedia.de" style="color:#888888;font:normal;text-decoration:none" target="_blank">texmedia.de<\/a><\/font>/", "offset" : "1 },
		]
		return(self.rules)

