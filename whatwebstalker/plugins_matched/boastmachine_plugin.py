import plugins
			
class Pluginboastmachine_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "powered by boastMachine" +"Recent posts"", "certainty" : "75 },
			{ "version" : "/Powered by <a href="http:\/\/boastology.com">boastMachine v([\d\.]+)<\/a>/" },
			{ "regexp" : "/<a href="http:\/\/boastology.com"><img src="http:\/\/[^>]*alt="Powered by boastMachine" \/><\/a>/" },
		]
		return(self.rules)
