import sys
import os
			
class Pluginxwiki_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="wiki" content="xwiki"/>" },
			{ "text" : "<div id="xwikilicence">" },
			{ "version" : "/<div id="xwikiplatformversion">(Powered by )?(XWiki Enterprise )?([^\s<>]+)/", "offset" : "2 },
		]
		return(self.rules)

