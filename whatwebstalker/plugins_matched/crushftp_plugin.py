import plugins
			
class Plugincrushftp_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "text" : "<script type="text/javascript" src="crushftp_functions.js"></script>" },
			{ "regexp" : "/^CrushFTP /", "search" : "headers[server]" },
			{ "version" : "/^CrushFTP (HTTP[\d]? Server )?Version ([\d\.]+)$/", "offset" : "1", "search" : "headers[server]" },
			{ "name" : "CrushAuth Cookie", "regexp" : "/^CrushAuth=/", "search" : "headers[set-cookie]" },
			{ "name" : "WWW-Authenticate", "version" : "/^Basic realm="CrushFTP Server Version ([\d\.]+)"$/", "search" : "headers[www-authenticate]" },
		]
	return(self.rules)

