import sys
import os
			
class Pluginbitcoin_js_remote_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "75", "text" : "<span id="balance"</span>" },
			{ "text" : "<p><a href="http://tcatm.github.com/bitcoin-js-remote">bitcoin-js-remote</a> <span id="version"></span> by <a href="mailto:tcatm@gawab.com">tcatm</a></p>" },
		]

