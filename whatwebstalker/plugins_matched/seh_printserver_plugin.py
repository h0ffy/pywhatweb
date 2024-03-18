import plugins
			
class Pluginseh_printserver_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/status/general_en.html", "model" : "/<TR><TD> Print server model<TD> ([^<]*)},
			{ "url" : "/status/general_en.html", "version" : "/<TR><TD> Software version<TD> ([^<]*)},
			{ "url" : "/status/general_en.html", "string" : /<TR><TD> Default print server name<TD> ([^<]*)},
		]
	return(self.rules)

