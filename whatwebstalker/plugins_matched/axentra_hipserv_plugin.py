import sys
import os
			
class axentra_hipserv_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="author" content="Axentra">' }
			{ "text" : '<title id="document_title">Axentra :: Digital Home/SOHO Software Platform for Internet Gateway and NAS Devices</title>' }
			{ "regexp" : '//", "search" : 'headers[x-axentra-version]" }
			{ "name" : 'HOMEBASEID Cookie", "regexp" : '/HOMEBASEID=/", "search" : 'headers[set-cookie]" }
		]

