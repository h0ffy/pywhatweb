b'''
import plugins

class Pluginedirectory_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : '<span class="basePowered">Powered by <a href="http://www.edirectory.com" target="_blank">eDirectory&trade;</a>.</span>' },
            { "regexp" : r'/ class="basePowered">Powered by <a href="[^"]+" target="_blank">eDirectory&trade;[\\s]?<\\/a>/' },
            { "version" : r'/<blockquote class="eDirectoryVersion"><span class="basePowered">Powered by <a href="http:\\/\\/www\\.edirectory\\.com" target="_blank">eDirectory&trade;<\\/a> <\\/span> v\\.([^<^\\s]+)<\\/blockquote>/' },
        ]
        return self.rules
'''