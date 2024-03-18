import plugins
			
class Pluginacollab_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>ACollab : Accessible Collaboration Environment:" },
		]
	return(self.rules)

