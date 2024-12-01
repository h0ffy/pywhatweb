```python
import plugins

class Pluginhighwire_press_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "search" : "headers[x-firenze-processing-time]", "regexp" : r"^[\\d\\.]+$" },
            { "search" : "headers[x-firenze-processing-tims]", "regexp" : r"^detect-robot:" },
            { "search" : "headers[x-highwire-sessionid]", "regexp" : r"^.+$" },
        ]
        return self.rules
```