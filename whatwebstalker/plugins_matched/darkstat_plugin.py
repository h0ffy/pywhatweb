import sys
import os
			
class darkstat_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<li class="label">darkstat ([^\s^<]+)<\/li><li><a href="[^"]+">graphs<\/a><\/li>/ }
			{ "version" : '/<title>darkstat ([^\s]+) : graphs ([^\s^\)]+)<\/title>/ }
			{ "search" : 'headers[server]", "version" : '/^darkstat\/([^\s]+)$/ }
		]

