import plugins
			
class Pluginwolfcms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/png" \/> Wolf CMS ([^<]+)<\/div>},
			{ "regexp" : "/href="http:\/\/www.wolfcms.org\/" title="Wolf CMS" rel="noreferrer">Wolf CMS<\/a>[\s]+Inside.},
		]
			return(self.rules)
