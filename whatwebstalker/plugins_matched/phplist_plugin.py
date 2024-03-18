import sys
import os
			
class phplist_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<html><head><title>Nothing here</title></head><body>' },
			{ "text" : '<p>You probably want to be <a href="../">here</a> or <a href="admin/">here</a>.</p>' },
			{ "text" : '<meta name="Author" content="Michiel Dethmers - http://www.phplist.com" />' },
			{ "version" : '/<meta name="Powered-By" content="phplist version ([^"]+)" \/>/ },
			{ "version" : '/<span class="urhere">phplist powered by <\/span><a class="urhere" href="http:\/\/www\.phplist\.com" target="_blank">phplist<\/a> - version ([^<]+)<\/td>/ },
		]

