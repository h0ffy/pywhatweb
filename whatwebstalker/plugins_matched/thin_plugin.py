import plugins
			
class Pluginthin_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^thin ([^\s]+) codename (.+)$/" },
			{ "search" : "headers[server]", "string" : /^thin [^\s]+ (codename .+)$/" },
		]
			return(self.rules)
