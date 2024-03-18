import plugins
			
class Pluginsubrion_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.subrion.com">Subrion CMS</a>" },
			{ "text" : "Powered by <strong><a href="http://www.subrion.com/" title="Subrion CMS" target="_blank">Subrion CMS</a>" },
			{ "text" : "powered by <a href="http://www.subrion.com/" title="Site powered by Subrion CMS">Subrion CMS</a>" },
			{ "version" : "/	<meta name="generator" content="Subrion CMS ([\d\.a-zA-Z]+)" \/>/" },
			{ "version" : "/	<title>Subrion CMS ([\d\.a-zA-Z]+) - Web Installer<\/title>/" },
			{ "version" : "/	Powered by <a href="http:\/\/www.subrion.com\/" title="Classifieds Software">Subrion CMS<\/a> Version ([\d\.a-zA-Z]+)<br \/>/" },
		]
		return(self.rules)

