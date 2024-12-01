import plugins
			
class Pluginericsson_tv_web_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server ]", "regexp" : "/^Ericsson Television Web server$/" },
		]
	return(self.rules)
