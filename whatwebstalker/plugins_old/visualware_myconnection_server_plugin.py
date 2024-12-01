import plugins
			
class Pluginvisualware_myconnection_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- Begin MyConnection Server applet -->" },
			{ "regexp" : "/^Visualware MyConnection Server/", "search" : "headers[server]" },
			{ "version" : "/^Visualware MyConnection Server [^\d]+ (\d\.[^\s]+)$/", "search" : "headers[server]" },
			{ "string" : /^Visualware MyConnection Server ([^\d]+) \d\.[^\s]+$/", "search" : "headers[server]" },
		]
	return(self.rules)
