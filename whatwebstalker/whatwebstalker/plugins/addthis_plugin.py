import plugins


class Pluginaddthis_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"regexp": "/<script [^>]*src=[\"|'][^>]*addthis\\.com\\/js/i"},
        ]
        return self.rules
