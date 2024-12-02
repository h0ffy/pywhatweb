import plugins


class Pluginrailo_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<script language = "JavaScript" type="text / javascript" src=" / railo - context / form.cfm"></script><script language = "JavaScript" type="text / javascript">"},
        ]
        return (self.rules)
