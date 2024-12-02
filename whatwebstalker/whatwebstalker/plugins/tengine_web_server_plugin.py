import plugins


class Plugintengine_web_server_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"search": "headers[server]", "regexp": "/^Tengine$/"},
            {"search": "headers[server]", "version": "/^Tengine\\/([^\\s]+)/"},
        ]
        return self.rules
