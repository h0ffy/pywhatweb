import plugins
			
class Pluginucenter_home_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by UCenter Home</title>" },
			{ "version" : "/Powered by <a  href="http:\/\/u.discuz.net" target="_blank"><strong>UCenter Home<\/strong><\/a> <span title="[0-9]{8}">([\d\.]+)<\/span>/" },
		]
		return(self.rules)
