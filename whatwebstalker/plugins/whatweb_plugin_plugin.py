import plugins


class Pluginwhatweb_plugin_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
        ]
        return (self.rules)
