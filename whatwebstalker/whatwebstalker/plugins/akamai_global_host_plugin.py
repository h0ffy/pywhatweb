import plugins
			
class Pluginakamai_global_host_plugin(plugins.Base):
    def __init__(self):
        super().__init__()
        self.rules = []

    def start(self):
        self.rules.append({ "search" : "headers[server]", "regexp" : "^AkamaiGHost" })
        return self.rules