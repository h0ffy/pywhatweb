import plugins
			
class Pluginisp_config_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/powered by <a HREF="http:\/\/www.ispconfig.org">ISPConfig<\/a>/i },
			{ "certainty" : "75", "text" : "This IP address is shared. For access to the web site which you look for", "enter its address instead of its IP." },
		]
	return(self.rules)
