import plugins
			
class Pluginzones_web_solution_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="author" content="Vikas Madaan (http://madaan.zones.in) - Zones Web Solution (www.zones.in)", "Visit http://www.zones.in for more info">" },
			{ "text" : "<br>Powered by : <a href="http://www.zones.in" target="_blank">Zones Web Solution</a> &amp;" },
		]
		return(self.rules)
