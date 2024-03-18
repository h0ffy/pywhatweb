import plugins
			
class Pluginoracle_application_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "string" : /^Oracle-Application-Server-(1[01]g)/" },
			{ "search" : "headers[server]", "version" : "/^Oracle-Application-Server-1[01]g\/([^\s]+)/" },
			{ "search" : "headers[server]", "version" : "/^Oracle Application Server\/1[01]g \(([^\s^\)]+)\)/" },
			{ "search" : "headers[server]", "module" : /^Oracle[ -]Application[ -]Server.+ (OracleAS-Web-Cache-1[01]g\/[^\s]+)/" },
		]
	return(self.rules)
