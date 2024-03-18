import sys
import os
			
class Pluginwinamp_web_interface_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "ghdb" : "About Winamp Web Interface" intitle:"Winamp Web Interface"", "certainty" : "75 },
			{ "text" : "<noframes><p><b>Frames are required for this site!<b></p><p>If no-frames operation is required", "check the <b>No Frames Mode</b> box in the Options screen.</p>" },
			{ "version" : "/<a href="JavaScript:about\(\)">About Winamp Web Interface v([\.\d]+)<\/a><\/h6><hr>/" },
		]

