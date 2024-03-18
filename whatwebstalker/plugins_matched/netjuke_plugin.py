import sys
import os
			
class Pluginnetjuke_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!-- Start Primary Header -->" },
			{ "text" : "<!-- Begin Primary Footer -->" },
			{ "text" : "onClick=\"window.open('alphabet.php?do=alpha.artists','NetjukeRemote'" },
		]

