import plugins


class Plugindavid_webbox_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {
                "search": "headers[server]",
                "version": "/^David-WebBox\\/([^\\s]+ \\([^\\)]+\\))$/",
            },
        ]
        return self.rules
