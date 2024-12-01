```python
import plugins

class Pluginduforum_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "certainty" : "75", "ghdb" : "+powered by duforum intitle:DUdforum" },
            { "name" : "default title", "regexp" : r"/<title>DUdforum[0-9a-zA-Z\s\.-]+<\/title>" },
        ]
        return self.rules
```