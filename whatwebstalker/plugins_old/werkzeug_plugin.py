import plugins
			
class Pluginwerkzeug_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Werkzeug\/([\d\.]+)/" },
			{ "status" : "302", "certainty" : "75", "text" : "<p>You should be redirected automatically to target URL:" },
		]
	return(self.rules)
