import sys
import os
			
class storagetek_nas_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : '/sedona.jnlp", "text" : '<title>Sun StorageTek NAS OS Web Admin</title>' }
			{ "regexp" : '/^StorageTek-HTTPD/", "search" : 'headers[server]" }
			{ "version" : '/^StorageTek-HTTPD\/([^\s]+) \([^\s]+ NAS\)$/", "search" : 'headers[server]" }
			{ "model" : '/^StorageTek-HTTPD\/[^\s]+ \(([^\s]+) NAS\)$/", "search" : 'headers[server]" }
	]

