import sys
import os
			
class Pluginxwiki_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<meta name="wiki" content="xwiki"/>" },
			{ "text" : "<div id="xwikilicence">" },
			{ "version" : "/<div id="xwikiplatformversion">(Powered by )?(XWiki Enterprise )?([^\s<>]+)/", "offset" : "2 },
		]

