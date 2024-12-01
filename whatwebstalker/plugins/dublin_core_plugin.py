```python
import plugins

class Plugindublin_core_plugin(plugins.Base):
    def __init__(self):
        pass
    def start(self):
        self.rules = [
            { "name" : "dublin core", "regexp" : r'/<meta [^>]*name="DC\.title"[^>]*>/i'},
        ]
        return self.rules
```