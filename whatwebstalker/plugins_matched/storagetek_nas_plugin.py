import plugins
			
class Pluginstoragetek_nas_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/sedona.jnlp", "text" : "<title>Sun StorageTek NAS OS Web Admin</title>" },
			{ "regexp" : "/^StorageTek-HTTPD/", "search" : "headers[server]" },
			{ "version" : "/^StorageTek-HTTPD\/([^\s]+) \([^\s]+ NAS\)$/", "search" : "headers[server]" },
			{ "model" : "/^StorageTek-HTTPD\/[^\s]+ \(([^\s]+) NAS\)$/", "search" : "headers[server]" },
		]
		return(self.rules)
