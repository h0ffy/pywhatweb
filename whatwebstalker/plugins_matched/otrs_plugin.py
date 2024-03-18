import sys
import os
			
class otrs_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'Powered by OTRS" inurl:customer.pl", "certainty" : '75 }
			{ "text" : '<title>OTRS  :: Login</title>' }
			{ "version" : '/Powered by <a href="http:\/\/otrs.org[\/]*" class="small">OTRS ([^<]+)<\/a>/ }
	]

