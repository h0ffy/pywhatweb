import plugins
			
class Pluginxbmc_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "		<!-- <link rel="search" href="/provider.xml" type="application/opensearchdescription+xml" title="XBMC Library" /> -->", "string" : "Insecure" },
			{ "url" : "/favicon.ico", "md5" : "46b742e6ba5d7ac03f13b312601c113f", "certainty" : "75 },
		]
	return(self.rules)
