import plugins
			
class Pluginmodlogan_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<link rel="stylesheet" href="modlogan.css" type="text/css" />" },
			{ "text" : "<LINK REL=STYLESHEET HREF="modlogan.css" type="text/css"></HEAD>" },
			{ "version" : "/Output generated by <a href="http:\/\/www\.(modlogan\.org|kneschke\.de\/projekte\/modlogan\/)">modlogan ([^\s^<]+)<\/a>/", "offset" : "1 },
		]
		return(self.rules)
