import plugins
			
class Pluginallnewsmanager.net_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/(kujeme|Powered by) <a id="[^"]+" href="http:\/\/www.allnewsmanager.net">AllNewsManager.NET<\/a>/" },
		]
	return(self.rules)

