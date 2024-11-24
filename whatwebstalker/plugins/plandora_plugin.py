import plugins


class Pluginplandora_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<area shape="rect" coords="180, 1, 215, 30" href="javascript: void(0)
             " onClick="closeFloatPanel()
             " />"},
        ]
        return (self.rules)
