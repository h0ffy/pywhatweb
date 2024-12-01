```python
import plugins

class Pluginibm_webseal_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "search" : "headers[server]", "version" : "/^WebSEAL\\/([^\\s]+ \\(Build \\d+\\))/" },
        ]
        return self.rules
```