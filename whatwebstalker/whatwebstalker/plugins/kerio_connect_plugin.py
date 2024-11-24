import plugins


class Pluginkerio_connect_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = []
        return self.rules
