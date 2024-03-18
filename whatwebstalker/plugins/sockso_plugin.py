import plugins
			
class Pluginsockso_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Sockso$/" },
			{ "version" : "/<p id="legal">[\s]+<strong>Sockso<\/strong>[\s]+v([^<]+)<br \/>[\s]+&copy; 20[\d]{2}/" },
		]
	return(self.rules)
