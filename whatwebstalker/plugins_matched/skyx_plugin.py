import sys
import os
			
class skyx_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<div id="skyx_status">SkyX status: enhancing</div>' }
			{ "text" : '<script language="javascript" type="text/javascript" src="/skyxgui.js"></script>' }
			{ "string" : /<div id="hostname"><a href="Misc">Hostname<\/a>: ([^\s^<]+)<\/div>/ }
			{ :"regxp" : '/^SkyX /", "search" : 'headers[server]" }
			{ "version" : '/^SkyX HTTPS ([^\s]+)$/", "search" : 'headers[server]" }
		]

