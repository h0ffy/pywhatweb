import sys
import os
			
class Pluginmioot_live_chat_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<div id="miootOnOffDiv"" },
			{ "text" : "<!-- Start LIVE CHAT image tag", "for details visit www.mioot.com -->" },
			{ "text" : "<a href="javascript:OnOffImage(\'V\')" " },
		]

