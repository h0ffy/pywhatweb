import sys
import os
			
class adobe_flash_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<object[^>]+application\/x-shockwave-flash[^>]+>/i },
			{ "regexp" : "/<embed[^>]+src[\s]*=[\s]*["']?[^\s^'^"^>]+/i },
			{ "regexp" : "/new[\s]+FlashObject[\s]*\([\s]*['"]?[^'^"]+/" },
			{ "regexp" : "/new[\s]+SWFObject[\s]*\([\s]*['"]?[^'^"]+/" },
			{ "regexp" : "/\.embedSWF[\s]*\([\s]*["']?[^'^"]+/" },
			{ "name" : "File extension", "regexp" : "/^(fla|flv|swf|swt|swc)$/", "search" : "uri.extension" },
		]

