import plugins
			
class Pluginm2soft_rdserver_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>M2Soft Report Designer Server</title>" },
			{ "url" : "/RDServer/rdagent.jsp", "version" : "/<font face="Verdana" size=2>\s+<li>Server version : ([^\s]+)/" },
			{ "search" : "headers[writereportlog]", "regexp" : "/^FALSE$/" },
			{ "search" : "headers[server]", "version" : "/^RDServer\/([^\s]+)$/" },
		]
		return(self.rules)
