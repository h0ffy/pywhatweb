import plugins


class Pluginsentinelserver_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"search": "headers[server]", "regexp": "/^SentinelServer/"},
        ]
        return self.rules
