import plugins
			
class Pluginmark_of_the_web_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "string" : /<!-- saved from url=\([\d]+\)([^>]+) -->[\r\n]/" },
		]
			return(self.rules)
