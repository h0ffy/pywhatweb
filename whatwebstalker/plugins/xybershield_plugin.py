import plugins


class Pluginxybershield_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {
                "search": "headers[set-cookie]",
                "regexp": "/XyberShieldSession=[^\\s]+;/",
            },
            {"search": "headers[set-cookie]", "regexp": "/XyberShieldStatus=[^\\s]+;/"},
        ]
        return self.rules
