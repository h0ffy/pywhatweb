import plugins
			
class Plugincups_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^CUPS\/([^\s]+)$/" },
			{ "search" : "headers[upgrade]", "regexp" : "/^TLS\/1\.0,HTTP\/1\.1$/", "certainty" : "25 },
		]
			return(self.rules)
