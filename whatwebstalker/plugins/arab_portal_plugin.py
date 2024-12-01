b'''
import plugins

class Pluginarab_portal_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : r'/<META NAME="COPYRIGHT" CONTENT="Copyright[^\\>]*by Arab[\\s]*Portal"/' },
            { "version" : r'/<META content="[^>]*Powered by: Arab Portal v([\\d\\.]+)", "Copyright[^>]*" name="description">/' },
            { "version" : r'/<center><font size=2>Powered by: Arab[\\s]*Portal v([\\d\\.]+)[\\s]*", "Copyright/' },
        ]
        return self.rules
'''