import plugins
			
class Pluginipmate_router_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<TITLE>Welcome to IPMATE</TITLE>" },
			{ "url" : "/images/ipmate_logo.gif", "md5" : "8d16375ac9c6c0fc1c27c0183dfda573" },
		]
	return(self.rules)
