import plugins
			
class Pluginpressflow_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<a href="http:\/\/drupal.org"><img src="[\/a-zA-Z0-9\-\_+]*\/misc\/powered-blue-80x15.png" alt="Powered by Pressflow", "an open source content management system" title="Powered by Pressflow", "an open source content management system" width="80" height="15" \/><\/a>/" },
			{ "text" : "<title>Drupal already installed | Pressflow</title>", "version" : "Install Page" },
		]
	return(self.rules)
