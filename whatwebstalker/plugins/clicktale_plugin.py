import plugins

class Pluginclicktale_plugin(plugins.Base):
    def __init__(self):
        pass
    def start(self):
        self.rules = [
            { "text" : '<div id="ClickTaleDiv" style="display: none;"></div>' },
        ]
        return self.rules