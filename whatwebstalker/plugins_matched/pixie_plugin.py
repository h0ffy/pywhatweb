import plugins
			
class Pluginpixie_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/href="http:\/\/www.getpixie.co.uk" title="Get Pixie">(Pixie Powered|Powered by Pixie|Pixie)<\/a>/" },
			{ "version" : "/<meta name="generator" content="Pixie ([\d\.]+) - Copyright \(C\) [\d]{4} - [\d]{4}\." \/>/" },
		]
	return(self.rules)
