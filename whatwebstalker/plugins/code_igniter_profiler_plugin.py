b'''
import plugins

class Plugincode_igniter_profiler_plugin(plugins.Base):
    def __init__(self):
        self.rules = []
        
    def start(self):
        return self.rules
'''