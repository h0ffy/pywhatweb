```python
import plugins

class Plugingoogle_analytics_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = []
        return self.rules
```