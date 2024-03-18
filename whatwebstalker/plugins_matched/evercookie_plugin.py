import sys
import os
			
class evercookie_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : "inurl:/evercookie.js filetype:js "\*  by samy kamkar : code@samy.pl : http://samy.pl"" },
			{ "version" : "/^ \* evercookie ([\d\.]{1,3}) \([\d]{2}\/[\d\.]{2}\/[\d\.]{4}\) -- extremely persistent cookies/" },
			{ "url" : "evercookie.js',"text" : "*  by samy kamkar : code@samy.pl : http://samy.pl'},
			{ "string" : /<script[^>]+src=['"]([^"^'^>]*evercookie\.js)['"][^>]*>[\s]*<\/script>/" },
		]

