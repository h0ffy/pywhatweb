import plugins


class Plugincovalent_enterprise_ready_server_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = []
        return self.rules
