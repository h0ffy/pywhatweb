import plugins
			
class Pluginscrewturn_wiki_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/Powered by <a class="externallink" href="http:\/\/www\.screwturn\.eu" title="ScrewTurn Wiki" target="_blank">ScrewTurn Wiki<\/a> version ([\d\.]+)/" },
		]
		return(self.rules)
