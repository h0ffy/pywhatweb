import plugins
			
class Pluginwikidforum_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.wikidforum.com" title="wikidforum.com">WikidForum</a>" },
		]
		return(self.rules)
