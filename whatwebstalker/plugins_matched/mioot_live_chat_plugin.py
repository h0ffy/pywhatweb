import sys
import os
			
class Pluginmioot_live_chat_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="miootOnOffDiv"" },
			{ "text" : "<!-- Start LIVE CHAT image tag", "for details visit www.mioot.com -->" },
			{ "text" : "<a href="javascript:OnOffImage(\'V\')" " },
		]
		return(self.rules)

