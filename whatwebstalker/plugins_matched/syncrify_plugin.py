import sys
import os
			
class syncrify_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "md5" : "b5a85ee65b5fda5f8180e1f9c2ab0560" },
			{ "url" : "/images/468x60.gif", "md5" : "2197210023deed6e71c704b6a27867a1" },
			{ "version" : "/<h3>Syncrify - <small>Version: ([\d\.]+ - build [\d]+)<\/small><\/h3>/" },
			{ "version" : "/<title>[\s]+Syncrify - Fast incremental backup - Version: ([\d\.]+ - build [\d]+) [\s]+<\/title>/" },
			{ "text" : "<meta NAME="Keywords" CONTENT="Syncrify - Fast incremental backup" />" },
			{ "text" : "<p>Powered by <a href='http://www.syncrify.com' >Syncrify</a></p>" },
		]

