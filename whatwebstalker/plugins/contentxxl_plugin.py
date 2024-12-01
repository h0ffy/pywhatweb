```python
import plugins

class Plugincontentxxl_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r'/<meta name="generator" content="contentXXL Business Content Management System  ([^\(]+)\([^\)]+\) \/ contentXXL International GmbH \/ www.contentxxl.de" [\/]?>/' },
            { "string" : r'/<meta name="generator" content="contentXXL Business Content Management System  [^\(]+\(([^\\)]+)", "[^,^>]+", "(Release|Debug)\) \/ contentXXL International GmbH \/ www.contentxxl.de" [\/]?>/' },
        ]
        return self.rules
```