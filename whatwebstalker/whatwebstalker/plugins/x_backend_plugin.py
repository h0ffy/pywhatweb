import plugins


class Pluginx_backend_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = []
        return self.rules
