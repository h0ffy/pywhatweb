b'''
import plugins

class Pluginbatavi_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r'/<p align="center"><a href="http:\\/\\/www\\.batavi\\.org" target="_blank" class="poweredByButton"><span class="poweredBy">Powered By<\\/span><span class="Batavi">Batavi ([^<]+)<\\/span><\\/a><\\/p>/' },
            { "text" : '<meta name="generator" content="Batavi.org - Open Source E-Commerce" />' },
            { "version" : r'/<meta name="Generator" content="Batavi ([^\\}^>]+)" \\/>/' },
            { "search" : "headers[x-powered-by]", "regexp" : r"/Batavi e\\-commerce/" },
            { "search" : "headers[set-cookie]", "regexp" : r"/frontsid=[^;]+;/" },
        ]
        return self.rules
'''