import plugins
			
class Pluginseportal_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<p align="center">[\r\n]*  Powered by <b>SePortal<\/b> ([\d\.]{1,5})[\r\n]*  <br \/>[\r\n]*  Copyright &copy; 20[\d]{2}-20[\d]{2} <a href="http:\/\/www.seportal.org" target="_blank">SePortal.org<\/a>[\r\n]*<\/p>/" },
			{ "text" : "  <title>SePortal Installer</title>" },
			{ "url" : "favicon.ico", "md5" : "9749740151cf551f80983ccebc6189f4" },
		]
		return(self.rules)

