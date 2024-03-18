import plugins
			
class Pluginhyperic_hq_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/ui_docs/DOC/index.html", "version" : "/<title>DOCS\d+ \(vFabric Hyperic ([^\)]+)\)/" },
			{ "text" : "<a id="screencastLink" href="http://www.hyperic.com/demo/screencasts.html" target="_blank" title="Screencasts">" },
			{ "search" : "headers[location]", "regexp" : "/\/app\/login;jsessionid=/" },
		]
		return(self.rules)
