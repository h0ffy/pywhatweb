import sys
import os
			
class Pluginopen_xchange_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<noscript><div class="noscriptmsg">You need to enable JavaScript to access the Open-Xchange Server." },
			{ "text" : "<td class="browserchecktextnormal" id="browserchecktext_id">You need to enable JavaScript to access the Open-Xchange Server." },
			{ "version" : "/<div class="login-bottomline">\W+<span id="[a-z]\d+[a-z]\d+">Version<\/span>\s+:\W+([^\s]+\W+[^\W]+)/" },
			{ "certainty" : "75", "search" : "headers[location]", "regexp" : "/^https?:\/\/[^\/]+\/ox6\/ox\.html$/", "version" : "6.x" },
		]

