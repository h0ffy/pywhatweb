b'''
import plugins

class Pluginapache_tomcat_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = []
        return self.rules
'''