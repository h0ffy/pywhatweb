import plugins


class Pluginkinja_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"name": "X-Kinja Header", "regexp": "/^$/", "search": "headers[x-kinja]"},
        ]
        return self.rules
