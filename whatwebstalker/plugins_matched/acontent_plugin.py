import sys
import os
			
class Pluginacontent_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>AContent: Learning Content Repository:" },
			{ "text" : "<dt><span class="required" title="Required Field">*</span><label for="login">Login Name or Email</label></dt>" },
			{ "md5" : "28c34462a074c5311492759435549468", "url" : "/favicon.ico" },
		]
		return(self.rules)

