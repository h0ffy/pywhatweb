import plugins
			
class Pluginwebalizer_log_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<!-- Generated by The Webalizer  Ver\. ([^\s]+) -->/" },
			{ "version" : "/<!-- Webalizer Version ([^\s]+) \(Mod: [\d]{1,2}-[a-zA-Z]{3}-[\d]{4}\) -->/" },
			{ "version" : "/<A HREF="http:\/\/www\.webalizer\.org\/"><STRONG>Webalizer Version ([^<]+)<\/STRONG><\/A>/" },
		]
		return(self.rules)
