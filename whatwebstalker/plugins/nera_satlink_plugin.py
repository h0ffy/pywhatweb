import plugins


class Pluginnera_satlink_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"search": "headers[www-authenticate]", "regexp": "/^Basic realm="SatLink Terminal"$/"},
        ]
        return (self.rules)
