import plugins
			
class Pluginpassword_field_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "rss link type", "regexp" : "/<input [^>]*?type=["']password["'][^>]*>/i },
		]
			return(self.rules)
