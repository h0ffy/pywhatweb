import plugins
			
class Pluginoracle_internet_application_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Oracle9iAS\/([^\s]+)/" },
			{ "search" : "headers[server]", "version" : "/^Oracle9iAS \(([^\s^\)]+)\)/" },
			{ "search" : "headers[server]", "module" : /^Oracle9iAS.+ (Oracle9iAS-Web-Cache\/[^\s]+)/" },
		]
		return(self.rules)
