import plugins
			
class Pluginwpquiz_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<title>[^>]*>> [Register|Login]+ - wp[q|Q]+uiz<\/title>/" },
		]
		return(self.rules)

