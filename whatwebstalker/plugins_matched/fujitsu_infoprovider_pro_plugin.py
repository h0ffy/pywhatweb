import plugins
			
class Pluginfujitsu_infoprovider_pro_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/Fujitsu-InfoProvider-Pro/" },
			{ "search" : "headers[server]", "version" : "/Fujitsu-InfoProvider-Pro\/[V]?([^ ]+) /" },
		]
			return(self.rules)
