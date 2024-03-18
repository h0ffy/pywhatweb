import plugins
			
class Pluginlaserwash_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "status" : "401", "search" : "headers[www-authenticate]", "regexp" : "/^Basic realm="PDQ Laserwash"$/" },
		]
		return(self.rules)
