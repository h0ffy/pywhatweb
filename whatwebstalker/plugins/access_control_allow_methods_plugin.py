import plugins
			
class Pluginaccess_control_allow_methods_plugin(plugins.Base):
    def __init__(self):
        self.rules = []

    def start(self):
        self.rules.append({ "search" : "headers[access-control-allow-methods]", "string" : "/(.+)/" })
        return self.rules