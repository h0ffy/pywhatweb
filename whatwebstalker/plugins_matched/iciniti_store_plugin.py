import plugins
			
class Pluginiciniti_store_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- START (content_stylesheet.inc) -->" },
		]
		return(self.rules)
