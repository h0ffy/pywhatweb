b'''
import plugins

class Pluginicom_router_plugin(plugins.Base):
    def __init__(self):
        self.rules = []
        pass
    def start(self):
        return self.rules
'''