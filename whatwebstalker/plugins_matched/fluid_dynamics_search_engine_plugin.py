import plugins
			
class Pluginfluid_dynamics_search_engine_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/Powered by the <a href="http:\/\/www.xav.com\/scripts\/search\/"[^>]*>Fluid Dynamics Search Engine<\/a> v([\d\.]+) &copy; 20[\d]{2}/" },
		]
			return(self.rules)
