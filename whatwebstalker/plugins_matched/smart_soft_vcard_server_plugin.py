import plugins
			
class Pluginsmart_soft_vcard_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Error</title></head><body><h1>403 - Directory browsing not allowed</h1><hr>SMART-SOFT VCard HTTP/SSL server" },
			{ "version" : "/<title>Error<\/title><\/head><body><h1>403 - Directory browsing not allowed<\/h1><hr>SMART-SOFT VCard HTTP\/SSL server \(([^\)]+)\)<br>/" },
			{ "string" : /<title>Error<\/title><\/head><body><h1>403 - Directory browsing not allowed<\/h1><hr>SMART-SOFT VCard HTTP\/SSL server \([^\)]+\)<br>Server - ([\w]+)/" },
			{ "regexp" : "/^SMART-SOFT VCard/", "search" : "headers[server]" },
			{ "version" : "/^SMART-SOFT VCard HTTP\/SSL server \(([^\)]+)\)$/", "search" : "headers[server]" },
			{ "name" : "Exception header", "regexp" : "/^Directory%20browsing%20not%20allowed$/", "search" : "headers[exception]" },
		]
			return(self.rules)
