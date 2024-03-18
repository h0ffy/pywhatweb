import plugins
			
class Plugincitrix_web_pn_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Citrix Web PN Server$/" },
		]
	return(self.rules)
