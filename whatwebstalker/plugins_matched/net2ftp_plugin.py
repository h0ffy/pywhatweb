import plugins
			
class Pluginnet2ftp_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "text" : "<title>net2ftp - a web based FTP client</title>" },
			{ "version" : "/<!-- net2ftp version ([^\s]+) -->/" },
			{ "text" : "<!-- End of net2ftp login form -->" },
		]
			return(self.rules)
