import sys
import os
			
class dzcp_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<script language="javascript" type="text\/javascript" src="..\/inc\/_templates_\/[^\/]+\/_js\/dzcp.js"><\/script>/" },
			{ "regexp" : "/<!--\[ DZCP .{1} by Frank "deV!L" Herrmann - www.dzcp.de \]-->/" },
			{ "regexp" : "/<!--\[ DZCP .{1} by Frank "deV!L" Herrmann - www.dzcp.de & Patrick "Richy" Richert - www.my-starmedia.de\]-->/" },
		]

