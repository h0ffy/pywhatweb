import plugins
			
class Pluginacollab_plugin(plugins.Base):
    def __init__(self):
    	super().__init__()
    def start(self):
        self.rules = [
			{ "text" : "<title>ACollab : Accessible Collaboration Environment:" },
		]
        return self.rules