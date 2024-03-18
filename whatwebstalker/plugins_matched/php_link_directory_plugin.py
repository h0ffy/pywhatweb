import plugins
			
class Pluginphp_link_directory_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "powered by phpLinkDirectory"", "certainty" : "25 },
			{ "regexp" : "/<a href="http:\/\/www.phplinkdirectory.com[^>]*Phplinkdirectory/i },
			{ "version" : "/<meta name="generator"[^>]*content="PHP Link Directory ([0-9\.]+)"/" },
		]
	return(self.rules)
