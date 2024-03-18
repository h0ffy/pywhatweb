import sys
import os
			
class edirectory_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<span class="basePowered">Powered by <a href="http://www.edirectory.com" target="_blank">eDirectory&trade;</a>.</span>' }
			{ "regexp" : '/ class="basePowered">Powered by <a href="[^"]+" target="_blank">eDirectory&trade;[\s]?<\/a>/ }
			{ "version" : '/<blockquote class="eDirectoryVersion"><span class="basePowered">Powered by <a href="http:\/\/www\.edirectory\.com" target="_blank">eDirectory&trade;<\/a> <\/span> v\.([^<^\s]+)<\/blockquote>/ }
		]

