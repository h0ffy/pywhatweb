import sys
import os
			
class Pluginminecraft_server_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<span>Map type:</span><select id="mode" onchange="show(1,$(\'#mode\').val())">", "os" : "MineOS (Linux)" },
			{ "text" : "<title>MineOS Admin Page</title>", "os" : "MineOS (Linux)" },
		]
		return(self.rules)

