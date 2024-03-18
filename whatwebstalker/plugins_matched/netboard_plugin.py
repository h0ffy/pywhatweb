import plugins
			
class Pluginnetboard_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "inurl:"cgi-sys/netboard.cgi" filetype:cgi" },
			{ "text" : "<td><form method=post action="netboard.cgi">" },
			{ "text" : "<td><form method=post action=netboard.cgi>" },
		]
	return(self.rules)
