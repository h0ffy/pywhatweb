import plugins

class Pluginaxel_device_plugin(plugins.Base):
    def __init__(self):
        self.rules = []
        pass

    def start(self):
        return self.rules
