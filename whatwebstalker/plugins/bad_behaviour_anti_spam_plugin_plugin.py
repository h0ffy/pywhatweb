b'''
import plugins

class Pluginbad_behaviour_anti_spam_plugin_plugin(plugins.Base):
    def __init__(self):
        self.rules = []
        pass

    def start(self):
        return self.rules
'''