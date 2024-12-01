b'''
import plugins

class Pluginbarracuda_load_balancer_plugin(plugins.Base):
    def __init__(self):
        self.rules = []
        
    def start(self):
        return self.rules
'''