import plugins
			
class Pluginetano_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "All Rights Reserved.<br />Powered by <a href="http://www.datemill.com" title="Etano community builder">Etano</a>.</p>" },
			{ "text" : "Etano</a>. All Rights Reserved.<br />" },
		]
		return(self.rules)
