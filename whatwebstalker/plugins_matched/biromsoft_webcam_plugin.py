import sys
import os
			
class Pluginbiromsoft_webcam_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<title>Biromsoft WebCam</title>", "certainty" : "75 },
			{ "regexp" : "/<area shape="rect" coords="[\d\-,]+" href="http:\/\/www.biromsoft.com" alt="Visit BiromSoft " title="Visit BiromSoft ">/" },
			{ "text" : "<area shape="rect" coords="22,26,151,102" href="http://www.biromsoft.com">" },
		]

