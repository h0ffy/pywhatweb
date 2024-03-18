import sys
import os
			
class gossamer_forum_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'Powered by Gossamer Forum filetype:cgi inurl:gforum.cgi" },
			{ "certainty" : '75", "text" : '<title>Gossamer Forum: An error occured!</title>' },
			{ "version" : '/Powered by <a href="http:\/\/www.gossamer-threads.com">Gossamer Forum v.([\d\.]+)<\/a>/ },
			{ "account" : '/<a href="gforum\.cgi\?username=([^;^>^"]+);guest=[\d]+">/ },
		]

