b'''
import plugins

class Pluginhaproxy_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "status" : "401", "search" : "headers[www-authenticate]", "text" : 'Basic realm="HAProxy Statistics"' },
        ]
        return self.rules
'''