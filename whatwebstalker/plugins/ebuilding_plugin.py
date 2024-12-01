```python
import plugins

class Pluginebuilding_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "certainty" : "75", "text" : "<title>eBuilding Web</title>" },
            { "url" : "/", "md5" : "fcfda4be8f50b3312b38966f2864188f" },
            { "text" : "<HTML><HEAD><TITLE>eBuilding Network Controller</TITLE><LINK title=global_style " },
        ]
        return self.rules
```