import plugins
			
class Plugin1n1_hosting_plugin(plugins.Base):
    def __init__(self):
        super().__init__()
        self.rules = []

    def start(self):
        return self.rules