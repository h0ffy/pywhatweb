import plugins

class Pluginhtml5_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : "<!DOCTYPE html>" },
            { "string" : "applicationCache", "regexp" : "<html[^>]* manifest=" },
        ]
        return self.rules