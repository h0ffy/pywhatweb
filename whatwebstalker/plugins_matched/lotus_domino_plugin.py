import plugins
			
class Pluginlotus_domino_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "ghdb" : "filetype:nsf" },
			{ "search" : "headers[server]", "version" : "/^Lotus-Domino\/([^\s]+)/" },
			{ "search" : "headers[server]", "regexp" : "/^Lotus-Domino$/" },
			{ "certainty" : "75", "url" : "/favicon.ico", "md5" : "639b61409215d770a99667b446c80ea1" },
		]
		return(self.rules)
