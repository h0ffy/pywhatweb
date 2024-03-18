import plugins
			
class Pluginxmb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- Powered by XMB " },
			{ "text" : "<!-- The XMB Group -->" },
		]
		return(self.rules)

