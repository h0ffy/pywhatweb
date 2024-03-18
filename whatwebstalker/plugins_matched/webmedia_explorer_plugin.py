import plugins
			
class Pluginwebmedia_explorer_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/Powered by <a href="http:\/\/www.webmediaexplorer.com[^>]*>webmedia explorer ([\d\.]+)<\/a>/i },
		]
	return(self.rules)
