import plugins
			
class Pluginakamai_global_host_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^AkamaiGHost/" },
		]
<<<<<<< HEAD
	return(self.rules)
=======
        return(self.rules)
>>>>>>> parent of c1541b4c (Merge branch 'main' of https://github.com/h0ffy/pywhatweb)
