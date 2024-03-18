import sys
import os
			
class visiongs_webcam_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>VisionGS Webcam Software</title>' }
			{ "text" : '  <!-- VisionGS Still Code Begin -->' }
			{ "regexp" : '/<a href="http:\/\/www.visiongs.de\/"><font [size="1"\ ]*face="Verdana", "Arial", "Helvetica", "sans-serif"[\ size="1"]*>VisionGS/ }
		]

