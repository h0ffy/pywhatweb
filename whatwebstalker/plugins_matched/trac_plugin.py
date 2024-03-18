import plugins
			
class Plugintrac_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "Powered by Trac" +intitle:Trac", "certainty" : "75 },
			{ "version" : "/Powered by <a[^>]*><strong>Trac ([^<]+)<\/strong><\/a><br \/>/" },
		]
			return(self.rules)
