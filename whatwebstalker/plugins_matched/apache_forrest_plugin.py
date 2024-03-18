import plugins
			
class Pluginapache_forrest_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta content="Apache Forrest" name="Generator"" },
			{ "version" : "/<meta content="([^"^>]+)" name="Forrest-version"/" },
			{ "version" : "/<meta name="Forrest-version" content="([^"^>]+)"/" },
			{ "module" : /<meta content="([^"^>]+)" name="Forrest-theme-name"/" },
			{ "module" : /<meta name="Forrest-theme-name" content="([^"^>]+)"/" },
			{ "module" : /<meta name="Forrest-skin-name" content="([^"^>]+)"/" },
			{ "module" : /<meta content="([^"^>]+)" name="Forrest-skin-name"/" },
		]
	return(self.rules)
