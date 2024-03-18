import sys
import os
			
class Pluginsdcms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<br>Powered By <a href=['"]http:\/\/www\.sdcms\.cn['"] target=['"]_blank['"]>SDCMS ([^<]+)<\/a>/" },
			{ "text" : "<dl id="con_three_1" class="index_photo">" },
		]
		return(self.rules)

