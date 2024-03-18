import plugins
			
class Pluginwowza_media_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<html><head><title>Wowza Media Server [\d]+ Monthly Edition ([\d\.]+ build[\d]+)<\/title><\/head><body>Wowza Media Server [\d]+ Monthly Edition ([\d\.]+ build[\d]+)<\/body><\/html>/" },
			{ "search" : "headers[www-authenticate]", "text" : "realm="Wowza Media Systems"" },
		]
	return(self.rules)
