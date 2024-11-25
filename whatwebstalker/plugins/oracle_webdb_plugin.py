import plugins
			
class Pluginoracle_webdb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Oracle_WebDb_Listener\/([^\s]+)/" },
			{ "search" : "headers[location]", "regexp" : "/^(https?:\/\/[^\/]+)?\/WebDB\/WEBDB\.home$/", "certainty" : "75 },
		]
	return(self.rules)
