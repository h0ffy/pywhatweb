import sys
import os
			
class geoserver_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<link rel="shortcut icon" href="resources/org.geoserver.web.GeoServerBasePage/favicon.ico"/>' },
			{ "text" : '<link href="resources/org.geoserver.web.GeoServerBasePage/favicon.ico" rel="shortcut icon"/>' },
			{ "regexp" : '/<body>[\s]+<p><b>Redirecting to the actual home page\.<\/b><\/p>[\s]+<p>If you're stuck here", "it means you don't have javascript[\s]+enabled\. Javascript is required to actually use the GeoServer admin console.<\/p>[\s]+<\/body>[\s]+<\/html>/ },
			{ "version" : '/<p>[\s]+<span>This GeoServer instance is running version <strong>([^<^\s]+)<\/strong>\. For more information please contact the <a href="[^"^>]*">administrator<\/a>\.<\/span>[\s]+<\/p>[\s]+<\/div>/ },
			{ "string" : /<div id="welcome">[\s]+<p>[\s]+This GeoServer belongs to <a><span>([^<]+)<\/span><\/a>\.[\s]+<\/p>/ },
		]

