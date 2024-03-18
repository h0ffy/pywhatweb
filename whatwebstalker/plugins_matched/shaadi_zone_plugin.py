import plugins
			
class Pluginshaadi_zone_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a href='http://www.vastal.com/' target='_blank'>Powered By Shaadi Zone</a>." },
			{ "text" : "Powered By <a href='http://www.vastal.com/' target=\"_blank\">Shaadi Zone</a>" },
		]
		return(self.rules)
