import plugins


class Pluginroxen_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"search": "headers[server]", "regexp": "/^Roxen$/"},
            {"search": "headers[server]", "version": "/^Roxen\\/([^\\s]+)$/"},
        ]
        return self.rules
