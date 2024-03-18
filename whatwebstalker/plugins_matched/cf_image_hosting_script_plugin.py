import sys
import os
			
class cf_image_hosting_script_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<p>Powered By <a href="http://codefuture.co.uk/projects/imagehost/" title="Free PHP Image Hosting Script">CF Image Hosting script</a>" },
			{ "version" : "/<p>Powered By <a href="http[s]*:\/\/codefuture.co.uk\/projects\/imagehost[\d\.]*[^>]+>CF Image Hosting script ([\d\.]+)<\/a>/" },
		]

