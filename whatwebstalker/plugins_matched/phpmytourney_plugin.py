import plugins
			
class Pluginphpmytourney_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href=\"http://phpmytourney.sourceforge.net/\"><font face='Arial' size='1'>phpMyTourney</font> </a>" },
			{ "text" : "ERROR : page not properly called" },
		]
	return(self.rules)
