import plugins
			
class Pluginsymantec_client_security_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- Symantec Client Security Web Based Installation -->" },
			{ "certainty" : "75", "string" : /<META NAME="Copyright" Content="Copyright (20[\d]{2}) Symantec Corporation">/" },
		]
	return(self.rules)

