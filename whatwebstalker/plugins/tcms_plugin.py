import plugins


class Plugintcms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"ghdb": "powered by TCMS"", "certainty" : "75},
        ]
        return (self.rules)
