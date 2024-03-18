import plugins
			
class Pluginphpdirector_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<a href="http:\/\/www.phpdirector.co.uk\/">Powered by PHP Director ([\d\.]+)<\/a>/" },
		]
		return(self.rules)
