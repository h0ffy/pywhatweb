```python
import plugins

class Pluginf3site_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : '<a href="http://compmaster.prv.pl" target="_blank">powered by F3Site</a></span>' },
            { "regexp" : r'/Powered by[^>]*<a[^>]*href="http:\\/\\/compmaster.prv.pl[^>]*>F3Site[^>]*<\\/a>/' },
            { "regexp" : r'/Powered by[^>]*<a[^>]*href="http:\\/\\/dhost.info\\/compmaste[^>]*>F3Site[^<]*<\\/a>/' },
            { "version" : r'/Powered by <a href="http:\\/\\/compmaster.prv.pl">F3Site v([\d\\.]+) plus<\\/a>/' },
        ]
        return self.rules
```