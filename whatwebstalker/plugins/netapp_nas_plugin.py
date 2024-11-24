import plugins


class Pluginnetapp_nas_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"search": "headers[server]", "version": "/^NetApp\\/(.+)$/"},
        ]
        return self.rules
