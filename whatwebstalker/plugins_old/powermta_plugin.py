import plugins
			
class Pluginpowermta_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "status" : "403", "text" : "<html><body>Access denied.  Please consult the http-access directive in the User's Guide for more information.</body></html>" },
			{ "certainty" : "25", "search" : "headers[www-authenticate]", "regexp" : "/^Basic realm="PowerMTA"$/" },
		]
	return(self.rules)
