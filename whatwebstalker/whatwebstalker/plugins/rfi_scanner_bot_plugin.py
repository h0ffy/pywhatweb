import plugins


class Pluginrfi_scanner_bot_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = []
        return self.rules
