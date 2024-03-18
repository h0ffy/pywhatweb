import sys
import os
			
class Pluginacontent_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<title>AContent: Learning Content Repository:" },
			{ "text" : "<dt><span class="required" title="Required Field">*</span><label for="login">Login Name or Email</label></dt>" },
			{ "md5" : "28c34462a074c5311492759435549468", "url" : "/favicon.ico" },
		]

