import plugins


class Pluginblackjumbodog_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"search": "headers[server]", "regexp": "/^BlackJumboDog$/"},
            {"search": "headers[server]", "version": "/^BlackJumboDog Version (.+)$/"},
        ]
        return (self.rules)
