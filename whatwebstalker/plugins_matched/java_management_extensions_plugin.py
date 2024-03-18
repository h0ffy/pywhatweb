import plugins
			
class Pluginjava_management_extensions_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+ [DEBUG|INFO]/" },
		]
		return(self.rules)
