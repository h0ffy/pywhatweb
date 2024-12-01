b'''
import plugins

class Pluginjava_password_log_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = []
        return self.rules
'''