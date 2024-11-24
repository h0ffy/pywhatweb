import plugins


class Pluginms_sdk_httpserver_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = []
        return self.rules
