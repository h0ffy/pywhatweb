b'''
import plugins

class Pluginflyspray_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : "<!-- Please don\'t remove this line - it helps promote Flyspray -->" },
            { "text" : '<a href="http://flyspray.org/" class="offsite">Powered by Flyspray</a>' },
        ]
        return self.rules
'''