```python
import plugins

class Pluginfluentnet_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "ghdb" : "powered by FluentCMS from DotContent", "certainty" : "75" },
            { "version" : r'/<meta name="GENERATOR" content="Fluent[CMS|NET]+ ([\d\.]+) /' },
        ]
        return self.rules
```