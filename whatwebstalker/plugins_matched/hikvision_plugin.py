import plugins
			
class Pluginhikvision_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Hikvision-Webs$/" },
		]
		return(self.rules)
