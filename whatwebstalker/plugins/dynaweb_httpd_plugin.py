b'''
import plugins

class Plugindynaweb_httpd_plugin(plugins.Base):
    def __init__(self):
        self.rules = []
        
    def start(self):
        return self.rules
'''