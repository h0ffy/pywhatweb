import plugins
			
class Pluginmapserver_4_windows_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>MS4W - MapServer 4 Windows</title>" },
			{ "version" : "/<h1>MS4W - MapServer 4 Windows - version ([^<]+)<\/h1>\s+<h2>Introduction<\/h2>/" },
		]
	return(self.rules)

