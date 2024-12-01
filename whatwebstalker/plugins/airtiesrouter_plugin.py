import plugins
			
class Pluginairtiesrouter_plugin(plugins.Base):
    def __init__(self):
        super().__init__()
        self.rules = []

    def start(self):
        self.rules.append({ "version" : "/<title>Airties ([^<]+)<" })
        return self.rules