```python
import plugins

class Plugininterred_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : "<meta name='(generator|GENERATOR)' content='InterRed V([^,]+)'", "url" : "http://www.interred.de/", "company" : "InterRed GmbH", "offset" : "1" },
            { "version" : "<!-- Created with InterRed V([^,]+)", "url" : "http://www.interred.de/", "company" : "by InterRed GmbH -->" },
        ]
        return self.rules
```