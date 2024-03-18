import plugins
			
class Pluginotrs_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "Powered by OTRS" inurl:customer.pl", "certainty" : "75 },
			{ "text" : "<title>OTRS  :: Login</title>" },
			{ "version" : "/Powered by <a href="http:\/\/otrs.org[\/]*" class="small">OTRS ([^<]+)<\/a>/" },
		]
			return(self.rules)
