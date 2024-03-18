import plugins
			
class Pluginzfeeder_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<span style="font-family: Verdana", "Arial", "Helvetica", "sans-serif; font-size: xx-small;">powered by <a href="http://zvonnews.sourceforge.net">zFeeder</a></span>" },
		]
	return(self.rules)
