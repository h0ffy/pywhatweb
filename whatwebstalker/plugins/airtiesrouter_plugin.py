import plugins
			
class Pluginairtiesrouter_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
<<<<<<< HEAD
			{ "version" : "/<title>Airties ([^<]+)<},
		]
	return(self.rules)
=======
			{ "version" : "/<title>Airties ([^<]+)<" },
		]
        return(self.rules)
>>>>>>> parent of c1541b4c (Merge branch 'main' of https://github.com/h0ffy/pywhatweb)
