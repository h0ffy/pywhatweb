import sys
import os
			
class kodi_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>Kodi</title>' },
			{ "text" : '<link rel="search" href="provider.xml" type="application/opensearchdescription+xml" title="Kodi Library" />' },
			{ "name" : 'favicon", "md5" : '91b72b23e7f499d6c09cb18c7b1278f1", "url" : '/favicon.ico' },
			{ "name" : 'xbmc.org found in /js/xbmc.launcher.js", "certainty" : '25", "text" : 'xbmc.org", "url" : '/js/xbmc.launcher.js' },
			{ "name" : 'WebInterface version from /addon.xml", ":"module" : /id="webinterface.default".*[\s]+version="([^"]+)"/", "url" : '/addon.xml' },
			{ "name" : 'XBMC JSON version from /addon.xml", "version" : '/^[\s]+<import addon="xbmc.json" version="([^"]+)"/", "url" : '/addon.xml' },
		]

