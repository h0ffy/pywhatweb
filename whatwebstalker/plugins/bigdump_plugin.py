```python
import plugins

class Pluginbigdump_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r"/<h1>BigDump: Staggered MySQL Dump Importer ver\. ([^\s^<]{2,6})<\/h1>/" },
            { "version" : r"/<title>BigDump ver\. ([^\s^<]{2,6})<\/title>/" },
        ]
        return self.rules
```