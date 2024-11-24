import plugins


class Pluginmobile_joomla_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"search": "headers[set-cookie]", "regexp": "/mjmarkup=deleted;/"},
        ]
        return self.rules
