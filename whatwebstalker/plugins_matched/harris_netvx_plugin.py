import plugins
			
class Pluginharris_netvx_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a href=" onclick=\'window.open("http://www.goahead.com")\' title="Powered by the GoAhead Web Server.">" },
		]
			return(self.rules)
