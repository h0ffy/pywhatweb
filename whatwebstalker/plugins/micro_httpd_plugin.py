import plugins
			
class Pluginmicro_httpd_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/micro_httpd/i },
		]
	return(self.rules)
