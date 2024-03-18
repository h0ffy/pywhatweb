import plugins
			
class Pluginzoom_search_engine_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<center><p><small>Search powered by <a href="http://www.wrensoft.com/zoom/" target="_blank"><b>Zoom Search Engine</b></a></small></p></center>" },
			{ "version" : "/<!--Zoom Search Engine Version ([\d\.]+ \([\d]+\) [A-Z]{3})-->/" },
			{ "version" : "/<!--Zoom Search Engine Version ([\d\.]+ \([\d]+\))-->/" },
		]
		return(self.rules)

