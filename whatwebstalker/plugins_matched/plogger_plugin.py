import plugins
			
class Pluginplogger_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<title>[^powered]+powered by Plogger Gallery<\/title>/" },
			{ "regexp" : "/<a[\ title="Powered by Plogger"]* href="http:\/\/www.plogger.org\/">Powered by Plogger[!]*<\/a>/" },
		]
	return(self.rules)
