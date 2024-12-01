import plugins
			
class Pluginmobilityguard_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/mg-local/cookie.html", "text" : "<font size=2>Click here for more information about MobilityGuard.</font></a></center><br>" },
		]
	return(self.rules)
