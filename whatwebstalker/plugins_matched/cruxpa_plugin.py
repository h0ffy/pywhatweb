import plugins
			
class Plugincruxpa_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="copy"><center>Powered By <a href="http://www.cruxsoftware.co.uk">CruxPA</a><br>" },
		]
	return(self.rules)

